A = list(map(float, input().split()))
pi = 3.14159

TRIANGULO = (A[0]*A[2]/2)
CIRCULO = pi*(A[2])**2
TRAPEZIO = ((A[0]+A[1])*A[2])/2 #((ভিত্তি ১ + ভিত্তি ২) × উচ্চতা) / ২
QUADRADO = A[1]**2
RETANGULO = A[0]*A[1]

print(f'TRIANGULO: {TRIANGULO:.3f}\nCIRCULO: {CIRCULO:.3f}\nTRAPEZIO: {TRAPEZIO:.3f}\nQUADRADO: {QUADRADO:.3f}\nRETANGULO: {RETANGULO:.3f}')
