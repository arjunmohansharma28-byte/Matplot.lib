import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
score = [68, 69, 66, 98, 76, 88, 99 ]
plt.bar(days, score, color="Red")
plt.title("My Quiz Tracker!")
plt.xlabel("Days in the Week")
plt.ylim(0, 100)
plt.ylabel("Scores")
plt.show()

