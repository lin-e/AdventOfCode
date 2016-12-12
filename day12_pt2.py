instructions = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5""".split('\n')
registers = dict()
registers["a"] = 0
registers["b"] = 0
registers["c"] = 1
registers["d"] = 0
instruction_index = 0
def read(item):
    global registers
    try:
        return int(item)
    except:
        return registers[item]
def execute(instruction):
    global instruction_index
    global registers
    parts = instruction.split()
    if parts[0] == "cpy":
        if parts[1] in registers:
            registers[parts[2]] = registers[parts[1]]
        else:
            registers[parts[2]] = int(parts[1])
    elif parts[0] == "inc":
        registers[parts[1]] += 1
    elif parts[0] == "dec":
        registers[parts[1]] += -1
    elif parts[0] == "jnz":
        if not read(parts[1]) == 0:
            instruction_index += int(parts[2])
            return True
    return False
while instruction_index < len(instructions):
    instruction = instructions[instruction_index]
    if execute(instruction):
        continue
    else:
        instruction_index += 1
print(registers)
