from ast import And, Not, Or
from email.mime import application
from email.quoprimime import body_check
from symtable import Symbol
from logic import * # type: ignore

rain = Symbol("rain") # It is raising.
hagrid = Symbol("hagrid") # Harry visited Hagrid.
dumbledore = Symbol("dumbledore") # Harry visited Dumbledor.

knowledge = any(
    application(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

model_check(knowledge, rain) # type: ignore
