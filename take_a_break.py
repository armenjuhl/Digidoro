import time
import webbrowser

total_breaks = 3
break_count = 1

print ("this program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(1200)
    webbrowser.open("https://www.youtube.com/watch?v=R5LYk0RlUrY")
    break_count += 1
    
if __name__ == '__main__':
    app.run()
