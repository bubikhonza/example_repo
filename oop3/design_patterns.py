from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache


class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.size = None
        self.topping = []


class PizzaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza()

    def with_dough(self, dough: str):
        self.pizza.dough = dough
        return self

    def with_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self

    def add_peperoni(self):
        if self.pizza.dough == "smetanovy":
            raise Exception("Cannot add salam to smetana")
        self.pizza.topping.append('peperoni')
        return self

    def add_cheese(self):
        self.pizza.topping.append('cheese')
        return self

    def build(self):
        return self.pizza


pizza_builder = PizzaBuilder()

honza_pizza = pizza_builder.with_sauce("rajcatova").add_peperoni().build()


class Circle():
    ...

class Square():
    ...

class Rectangle():
    ...

class ShapeFactory:
    @staticmethod
    def create_shape(shape: str):
        if shape == "square":
            return Square()
        elif shape == "rectangle":
            return Rectangle()
        elif shape == "circle":
            return Circle()
        else:
            raise Exception(f"Unknown shape: {shape}")


circle = ShapeFactory.create_shape("circle")
square = ShapeFactory.create_shape("square")

class PizzaEnum(Enum):
    MARGARITA = "MARGARITA"
    QUATRO_FORMA = "QUATRO_FORMA"
    SALAMI = "SALAMI"

class PizzaFactory:
    @staticmethod
    def make_pizza(pizza_type: PizzaEnum) -> Pizza:
        pizza_builder = PizzaBuilder()
        if pizza_type == PizzaEnum.MARGARITA:
            ...
        elif pizza_type == PizzaEnum.QUATRO_FORMA:
            ...
        elif pizza_type == PizzaEnum.SALAMI:
            return pizza_builder.with_dough("obyc").with_sauce("rajcata").add_peperoni().add_cheese().build()


PizzaFactory.make_pizza(PizzaEnum.MARGARITA)

class Coffee:
    def cost(self):
        return 20

class MilkDecorator:
    def __init__(self, coffee):
        self.__coffee = coffee

    def cost(self):
        return self.__coffee.cost() + 10

class CreamDecorator:
    def __init__(self, coffee):
        self.__coffee = coffee

    def cost(self):
        return self.__coffee.cost() + 30

coffee = Coffee()
coffee = MilkDecorator(MilkDecorator(coffee))
coffee = CreamDecorator(coffee)
print(coffee.cost())

class AbstractPaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

class ApplePayPaymentStrategy(AbstractPaymentStrategy):
    def pay(self):
        print("Apple pay payment")

class GooglePayPaymentStrategy(AbstractPaymentStrategy):
    def pay(self):
        print("Google pay payment")

class PaypalPayPaymentStrategy(AbstractPaymentStrategy):
    def pay(self):
        print("Paypal pay payment")

class PaymentGateway:
    def __init__(self, payment_strategy: AbstractPaymentStrategy):
        self.__payment_strategy = payment_strategy
    def pay(self):
        self.__payment_strategy.pay()


gateway = PaymentGateway(payment_strategy=GooglePayPaymentStrategy())
gateway.pay()

gateway = PaymentGateway(payment_strategy=ApplePayPaymentStrategy())
gateway.pay()




class Publisher:
    def __init__(self):
        self.__subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.__subscribers.remove(subscriber)

    def send_message(self, message: str):
        for subscriber in self.__subscribers:
            subscriber.update(message)

class Subscriber:
    def update(self, message: str):
        print(f"I GOT THE MESSAGE {message}")


subscriber = Subscriber()
subscriber2 = Subscriber()
subscriber3 = Subscriber()
subscriber4 = Subscriber()

publisher = Publisher()

publisher.add_subscriber(subscriber)
publisher.add_subscriber(subscriber2)
publisher.add_subscriber(subscriber3)
publisher.add_subscriber(subscriber4)

publisher.send_message("New video, link here: ....")

class SingletonWithLru:
    ...

@lru_cache
def create_singleton_with_lru() -> SingletonWithLru:
    return SingletonWithLru()


object1 = create_singleton_with_lru()
object2 = create_singleton_with_lru()
object3 = create_singleton_with_lru()


print("asdasd")

queue_consumer = create_singleton_with_lru()


