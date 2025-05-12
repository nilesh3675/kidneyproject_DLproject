import sys
import os
sys.path.append(os.getcwd()) 

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_eval_04 import Evaluation
from cnnClassifier import logger
import os
import mlflow


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/nilesh3675/kidneyproject_DLproject.mlflow"
        os.environ["MLFLOW_TRACKING_USERNAME"]="nilesh3675"
        os.environ["MLFLOW_TRACKING_PASSWORD"]="a422041edabd6d8d628ff4d72ac34ee7bb0c11f2"

        # # Set MLflow tracking URI
        mlflow.set_tracking_uri("https://dagshub.com/nilesh3675/kidneyproject_DLproject.mlflow")
        evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e