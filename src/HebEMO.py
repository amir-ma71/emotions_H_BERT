from transformers import pipeline


class HebEMO:
    def __init__(self, device=-1, emotions=['anticipation', 'joy', 'trust', 'fear', 'surprise', 'anger',
                                            'sadness', 'disgust']):
        self.device = device
        self.emotions = emotions
        self.hebemo_models = {}
        print("Load models ...")
        for emo in emotions:
            self.hebemo_models[emo] = pipeline(
                "sentiment-analysis",
                model="./src/emotions_model/hebEMO_" + emo,
                tokenizer="./src/heBERT",
                device=self.device  # -1 run on CPU, else - device ID
            )
            print(emo , " Done . . .")
    def hebemo(self, text=None, input_path=False, save_results=False, read_lines=False, plot=False, pyplutchik=None):
        '''
        text (str): a text or list of text to analyze
        input_path(str): the path to the text file (txt file, each row for different instance)
        '''
        emo_dict = {}

        # run hebEMO
        for emo in self.emotions:
            x = self.hebemo_models[emo](text)
            if x[0]["label"] == "LABEL_1":
                score = x[0]["score"]
            else:
                score = 1 - x[0]["score"]

            emo_dict[emo] = float("%.2f" % score)
            del x

        return (emo_dict)
