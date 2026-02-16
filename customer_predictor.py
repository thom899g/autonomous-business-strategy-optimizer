import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import Dict, Optional

class CustomerBehaviorPredictor:
    def __init__(self):
        self.model = None
        self.data = None
    
    def preprocess_data(self) -> bool:
        """Preprocesses customer data for prediction."""
        try:
            # Example preprocessing steps
            if 'label' not in self.data.columns:
                raise ValueError("Label column 'label' is missing.")
            
            X = self.data.drop('label', axis=1)
            y = self.data['label']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            
            return True
        except Exception as e:
            print(f"Preprocessing failed: {str(e)}")
            return False
    
    def train_model(self) -> bool:
        """Trains the customer behavior prediction model."""
        try:
            if self.model is None:
                from sklearn.tree import DecisionTreeClassifier
                self.model = DecisionTreeClassifier()
            
            if self.data is None or not isinstance(self.data, pd.DataFrame):
                raise ValueError("Data not properly loaded.")
            
            X_train, X_test, y_train, y_test = self.preprocess_data()
            if not X_train:
                raise ValueError("No training data available.")
            
            self.model.fit(X_train, y_train)
            print(f"Model trained with accuracy: {self.model.score(X_test, y_test):.2f}")
            return True
        except Exception as e:
            print(f"Training failed: {str(e)}")
            return False
    
    def predict_behavior(self, data_point: Dict[str, float]) -> str:
        """Predicts customer behavior based on input data."""
        if not self.model or not self.data:
            raise ValueError("Model not trained or data not loaded.")
        
        try:
            # Example prediction
            prediction = self.model.predict([list(data_point.values())])
            return self.get_label_name(prediction[0])
        except Exception as e:
            print(f"Prediction failed: {str(e)}")
            raise
    
    def get_label_name(self, label_code: int) -> str:
        """Converts label code to human-readable behavior."""
        label_map = {
            0: 'Unlikely to purchase',
            1: 'Likely to purchase',
            2: 'High engagement'
        }
        return label_map.get(label_code, 'Unknown')

# Example usage
if __name__ == "__main__":
    predictor = CustomerBehaviorPredictor()
    # Assume data is loaded from a source
    predictor.data = pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.randint(0, 2, 100),
        'label': np.random.randint(0, 3, 100)
    })
    if predictor.train_model():
        print(predictor.predict_behavior({'feature1': 0.5, 'feature2': 1}))