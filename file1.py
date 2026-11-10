import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
score = [68, 69, 66, 98, 76, 88, 99 ]
plt.plot(days, score)
plt.show()


plt.plot(days, score)
plt.title("My Quiz Tracker!")
plt.xlabel("Days in the Week")
plt.ylabel("Scores")
plt.show()


plt.plot(days, score, color="blue", marker="o", linestyle="dashed", linewidth=2)
plt.title("My Quiz Tracker!")
plt.xlabel("Days in the Week")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0, 100)
plt.show()


plt.bar(days, score)
plt.title("My Quiz Tracker!")
plt.xlabel("Days in the Week")
plt.ylim(0, 100)
plt.ylabel("Scores")
plt.show()