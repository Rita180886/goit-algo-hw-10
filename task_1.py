from pulp import LpProblem, LpVariable, LpMaximize, value, PULP_CBC_CMD

def main():
    model = LpProblem("production_optimization", LpMaximize)

    lemonade = LpVariable("lemonade", lowBound=0, cat="Integer")
    fruit_juice = LpVariable("fruit_juice", lowBound=0, cat="Integer")

    model += lemonade + fruit_juice, "total_production"

    model += 2 * lemonade + 1 * fruit_juice <= 100
    model += 1 * lemonade <= 50
    model += 1 * lemonade <= 30
    model += 2 * fruit_juice <= 40

    model.solve(PULP_CBC_CMD(msg=False))

    print("Оптимальний план виробництва:")
    print(f"  Лимонад: {value(lemonade)} од.")
    print(f"  Фруктовий сік: {value(fruit_juice)} од.")
    print()
    print(f"Загальна кількість продукції: {value(lemonade + fruit_juice)} од.")

if __name__ == "__main__":
    main()