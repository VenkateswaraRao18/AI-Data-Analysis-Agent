from sklearn.feature_extraction.text import TfidfVectorizer


class TextTool:

    def process_text(self, df, text_columns):

        vectorizer = TfidfVectorizer(max_features=500)

        for col in text_columns:

            text_features = vectorizer.fit_transform(df[col].astype(str))

            text_df = text_features.toarray()

            # drop original text column
            df = df.drop(columns=[col])

        return df