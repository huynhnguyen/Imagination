
class BatchTrainer:
    def __init__(self):
        None
    def __call__(self):
        None
    def train_on_batch(self):
        None
    def test_on_batch(self):
        None
    def eval_on_batch(self):
        None

class ModelTrainer(BatchTrainer):
    def __init__(self):
        None
    def should_save_image(self):
        None
    def should_save_checkpoint(self):
        None
    def train(self):
        None