import twint
import matplotlib.pyplot as plot
from datetime import datetime
import matplotlib.animation as animation
import os

def lastminute(keyword):


    minute = int(datetime.today().strftime('%M')-1)
    if minute < 10:
        minute = "0" + str(minute) 

    oneminuteago = datetime.today().strftime('%Y-%m-%d %H:') + minute + datetime.today().strftime(':%S')

    
    c = twint.Config()
    c.Search = keyword
    c.Since = oneminuteago
    c.Output = 'result.csv'
    c.Hide_output = True
    c.Count = True

    twint.run.Search(c)

    count = 0

    with open("result.csv", encoding = 'utf8') as file:
        count = sum(1 for line in file)
    
    os.remove('result.csv')

    return count, oneminuteago

# def initializegraph(label, x_vals, y_vals):
#     plot.plot(x_vals, y_vals)
#     plot.ylabel('Number of tweets of ' + label + 'in the last minute')
#     plot.xlabel('Time')

#     plot.show()

x_vals = []
y_vals = []

def animategraph(i):
    count, oneminuteago = lastminute('dogecoin')
    x_vals.append(oneminuteago)
    y_vals.append(count)
    print(x_vals, y_vals)

    plot.cla()

    plot.plot(x_vals, y_vals)



# while True:

# count, oneminuteago = lastminute('dogecoin')


# x_vals.append(oneminuteago)
# y_vals.append(count)
# initializegraph('dogecoin', x_vals, y_vals)

# plot.cla()

animate = animation.FuncAnimation(plot.gcf(), animategraph, interval = 0)
plot.show()



 