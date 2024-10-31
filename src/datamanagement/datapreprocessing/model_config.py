SPAM_HAM_LABELS = {"LABEL_1": "ham", "LABEL_0": "spam"}
SARCASM_LABELS = {"LABEL_1": "sarcastic", "LABEL_0": "not sarcastic" }
ARGUMENT_LABELS = {"LABEL_1": "non argument", "LABEL_0": "argument" }
model_configuration = {
                        "emotions":
                        {
                            "task": "text-classification", 
                            "model": "SamLowe/roberta-base-go_emotions",
                            "device": 0,
                        },
                        "fake-real":  {
                                 "task": "text-classification", 
                                 "model":"openai-community/roberta-base-openai-detector",
                                 "device": 0,
                            
                        },
                        "hate-no_hate":{
                                 "task": "text-classification",
                                 "model":"facebook/roberta-hate-speech-dynabench-r4-target",
                                 "device": 0,
                            },

                        "spam-ham": {
                                 "task": "text-classification",
                                 "model":"mshenoda/roberta-spam", # https://huggingface.co/mshenoda/roberta-spam
                                 # accurracy 0.99
                                 "device": 0,
                            },
                        "sarcasm": 
                            {
                                 "task": "text-classification",
                                 "model":"helinivan/english-sarcasm-detector",
                                # accurracy 0.92 https://huggingface.co/helinivan/english-sarcasm-detector
                                 "device": 0,
                            },
                        "fake_news": {
                                 "task": "text-classification",
                                #  "model":"mrm8488/bert-tiny-finetuned-fake-news-detection",
                                 "model":"hamzab/roberta-fake-news-classification",
                                # accurracy 0.99 https://huggingface.co/hamzab/roberta-fake-news-classification
                                 "device": 0,
                        },
                        "toxicity": {

                                 "task": "text-classification",
                                 "model":"unitary/toxic-bert",
                                 # accurracy 0.91 https://huggingface.co/unitary/toxic-bert
                                 "device": 0,
                        },
                        "offensive_detection": {
                                 "task": "text-classification",
                                 "model":"alexandrainst/da-offensive-detection-base",
                                 # accurracy 0.86  https://huggingface.co/alexandrainst/da-offensive-detection-base
                                 "device": 0,
                        },
                        "argument": {
                                 "task": "text-classification",
                                 "model":"chkla/roberta-argument",
                                 # accuracy 0.8193 https://huggingface.co/chkla/roberta-argument
                                 "device": 0,
                        },
                        "irony": {
                                 "task": "text-classification",
                                 "model":"pysentimiento/bertweet-irony",
                                 # accuracy 0.808 https://huggingface.co/pysentimiento/bertweet-irony
                                 "device": 0,
                        },
                        "subjectivity-objectivity ": {
                                 "task": "text-classification",
                                 "model":"GroNLP/mdebertav3-subjectivity-english",
                                 # accuracy 0.79 https://huggingface.co/GroNLP/mdebertav3-subjectivity-english
                                 "device": 0,
                        },
                        "intent": {
                                 "task": "text-classification",
                                 "model":"Falconsai/intent_classification",
                                 # accuracy 0.99 https://huggingface.co/Falconsai/intent_classification
                                 "device": 0,
                        },
                        "political_bias": {
                                 "task": "text-classification",
                                 "model":"bucketresearch/politicalBiasBERT",
                                 # accuracy 0.9 https://huggingface.co/premsa/political-bias-prediction-allsides-BERT
                                 "device": 0,
                        },
                    }
                    