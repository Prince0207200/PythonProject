class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        # Nicely format output like "4 + 6i" or "4 - 6i"
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imaginary)}i"


# 🔽 Testing
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(c1 + c2)      # Output: 4 + 6i
print(c1 - c2)      # Output: 2 + 2i
print(c1 == c2)     # Output: False
