import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
# Seed the random number generator.
# This ensures that the results below are reproducible.
contact = np.array([74, 75, 73, 76, 77, 78, 80, 80, 82, 82,
	       110, 95, 85, 80, 78, 79, 79, 79, 80, 85])
contactless = np.array([67, 72, 76, 78, 73, 78, 80, 72, 78, 78,
			   101, 94, 84, 80, 85, 85, 74, 75, 80, 90])

# plt.xlabel('Частота сердечных сокращений, уд/мин')
# plt.ylabel('Частота встречаемости')
# plt.hist(contactless)
# plt.show()

contact_bp = np.array([104, 101, 102, 100, 103, 105, 105, 107, 107, 146,
	       119, 116, 118, 109, 108, 102, 107, 109, 102, 105])
contactless_bp = np.array([95, 91, 93, 80, 82, 98, 123, 117, 93, 120,
			   105, 100, 111, 99, 104, 95, 109, 101, 117, 98])

plt.xlabel('Систолическое артериальное давление, мм рт. ст.')
plt.ylabel('Частота встречаемости')
plt.hist(contactless_bp)
plt.show()


measurements = [contact_bp, contactless_bp]

# print(np.std(contactless_bp-contact_bp))
# #boxplot
# fig7, ax7 = plt.subplots()
# ax7.boxplot(measurements)
# plt.show()

#bland-atman
# f, ax = plt.subplots(1, figsize = (8,5))
# sm.graphics.mean_diff_plot(contact_bp, contactless_bp, ax = ax)
# plt.show()