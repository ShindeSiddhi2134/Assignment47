from sklearn.linear_model import LinearRegression

def main():
    X = [
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
    ]

    Y = [50, 55, 60, 65, 70]

    Model = LinearRegression()
    Model.fit(X, Y)

    print("Coefficients:", Model.coef_)
    print("Intercept:", Model.intercept_)

if __name__ == "__main__":
    main()
