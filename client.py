from sentence_parser import Parser


OPERACION = "5 + IV - 3 + VII - 2"
# OPERACION = "V + IV - III + 7 - II"
# OPERACION= "CIX + V"
# OPERACION = "CIX + V - 3 + VII - 2"
# OPERACION = "MMMCMXCIX - CXIX + MCXXII - MMMCDXII - XVIII - CCXXXV"
# OPERACION = input()

print(OPERACION)

AST_ROOT = Parser.parse(OPERACION)

# Llamado al interprte recursivamente
print(AST_ROOT.interpret())

# Impresion de la representacion de la raiz
