from car_functions import *

def main():
    car_model = car('kia', 'soul', model_year='2015', color='black', tow_package='False',)
    for vehicle, info in car_model.items():
        print(f"{vehicle.title()}: {info.title()}")

if __name__ == "__main__":
    main()