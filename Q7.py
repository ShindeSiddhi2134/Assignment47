from sklearn.linear_model import LinearRegression

def main():
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]

    Model = LinearRegression()
    Model.fit(X, Y)

    print("Coefficient:", Model.coef_[0])
    print("Intercept:", Model.intercept_)

if __name__ == "__main__":
    main()
