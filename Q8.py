from sklearn.linear_model import LinearRegression

def main():
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]


    Model = LinearRegression()
    Model.fit(X, Y)

    Prediction = Model.predict([[6]])

    print("Predicted Marks:", Prediction[0])


if __name__ == "__main__":
    main()
