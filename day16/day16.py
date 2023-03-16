with open('input.txt')as file:
    input = file.read().split("\n\n")

ticket_fields = input[0].splitlines()
your_ticekts = input[1].split(":")[1]
nearby_tickets = input[2].split(":")[1].replace('\n',',')[1:-1].split(',')
nearby_tickets = [int(ticket) for ticket in nearby_tickets]

print(nearby_tickets)

fields_dict = {}
for line in ticket_fields:
    key = line.split(':')[0]
    value = line.split(': ')[1].split(' or ')
    fields_dict[key] = value
    
fields_dict     

def invalid_counter(value, ticket):

    count = 0
    for n in value:
        min, max = n.split('-')
        print('min:', min)
        print('max:', max)

        if min < str(ticket) < max:
            count += ticket
            print(min, ticket, max)
    return count

ticket = 50
value = ['48-206', '226-965']
    
print(invalid_counter(value, ticket))