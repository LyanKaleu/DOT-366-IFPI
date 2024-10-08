def celsius(temperatura_fahrenheit):
    return ((temperatura_fahrenheit - 32) / 9) * 5


def main():
    while True:
        try:
            temp_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
            print(f'Temperatura em Celsius: {celsius(temp_fahrenheit):.2f}°C')
            break
        except ValueError:
            continue


if __name__ == '__main__':
    main()
