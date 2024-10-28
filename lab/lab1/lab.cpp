#include <iostream>
#include <cmath>
#include <limits>

void discriminant(double a, double b, double c) {
    double d = b * b - 4 * a * c;

    if (d > 0) {
        double t1 = (-b + std::sqrt(d)) / (2 * a);
        double t2 = (-b - std::sqrt(d)) / (2 * a);

        if (t1 >= 0) {
            double x1 = std::sqrt(t1);
            double x2 = -std::sqrt(t1);
            std::cout << "x1: " << x1 << ", x2: " << x2 << "\n";
        }

        if (t2 >= 0) {
            double x3 = std::sqrt(t2);
            double x4 = -std::sqrt(t2);
            std::cout << "x3: " << x3 << ", x4: " << x4 << "\n";
        }

        if (t1 < 0 && t2 < 0) {
            std::cout << "No roots\n";
        }

    } else if (d == 0) {
        double x0 = -b / (2 * a);

        if (x0 >= 0) {
            double x1 = std::sqrt(x0);
            double x2 = -std::sqrt(x0);
            std::cout << "x1: " << x1 << ", x2: " << x2 << "\n";
        } else {
            std::cout << "No roots\n";
        }

    } else {
        std::cout << "Discriminant < 0, no roots\n";
    }
}

double getCoefficient(const std::string& prompt) {
    double coeff;
    while (true) {
        std::cout << prompt;
        if (std::cin >> coeff) break;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    return coeff;
}

int main() {
    setlocale(LC_ALL, "Russian");
    double a = getCoefficient("Enter coef a: ");
    double b = getCoefficient("Enter coef b: ");
    double c = getCoefficient("Enter coef c: ");

    discriminant(a, b, c);

    return 0;
}
