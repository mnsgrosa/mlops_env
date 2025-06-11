from sklearn.neighbors import LocalOutlierFactor
from scipy.stats import shapiro

class OutlierDetector:
    def __init__(self):
        self.province_model = LocalOutlierFactor()
        self.city_model = LocalOutlierFactor()
        self.shapiro_threshold = 0.05

    def fit_province(self, X):
        self.province_model.fit(X)

    def fit_city(self, X):
        self.city_model.fit(X)

    def predict_province(self, X):
        return self.province_model.predict(X)

    def predict_city(self, X):
        return self.city_model.predict(X)

    def is_normal(self, X):
        if len(X) < 2:
            return False
        _, p = shapiro(X)
        return p > self.shapiro_threshold