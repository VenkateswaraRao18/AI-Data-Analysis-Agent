from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd


class MLTool:

    def detect_problem_type(self, df, target):

        if df[target].nunique() <= 10:
            return "classification"
        else:
            return "regression"

    def run(self, dataset_path):

        df = pd.read_csv(dataset_path)

        target = df.columns[-1]

        X = df.drop(columns=[target])
        y = df[target]

        if y.dtype == "object":
            le = LabelEncoder()
            y = le.fit_transform(y)

        X = pd.get_dummies(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        problem_type = self.detect_problem_type(df, target)

        results = {}

        if problem_type == "classification":

            models = {
                "Logistic Regression": LogisticRegression(max_iter=2000),
                "Random Forest": RandomForestClassifier()
            }

            for name, model in models.items():

                model.fit(X_train, y_train)

                preds = model.predict(X_test)

                score = accuracy_score(y_test, preds)

                results[name] = score

        else:

            models = {
                "Linear Regression": LinearRegression(),
                "Random Forest Regressor": RandomForestRegressor()
            }

            for name, model in models.items():

                model.fit(X_train, y_train)

                preds = model.predict(X_test)

                score = r2_score(y_test, preds)

                results[name] = score

        # ---- detect best model ----

        best_model = max(results, key=results.get)

        return {
            "problem_type": problem_type,
            "results": results,
            "best_model": best_model,
            "target": target
        }