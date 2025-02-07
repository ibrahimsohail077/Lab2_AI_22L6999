
import matplotlib.pyplot as plt
import numpy as np


group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15, 40, 45, 50, 62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]


fig, axes = plt.subplots(1, 2, figsize=(10, 5))  

axes[0].boxplot(group_A, vert=False, patch_artist=True)
axes[0].set_title('Box Plot of Group A')
axes[0].set_xlabel('Measurement Values')
axes[0].set_yticklabels([]) 


axes[1].boxplot(group_B, vert=False, patch_artist=True)
axes[1].set_title('Box Plot of Group B')
axes[1].set_xlabel('Measurement Values')
axes[1].set_yticklabels([]) 


fig.suptitle('Box Plots of Group A and Group B')


plt.tight_layout(rect=[0, 0.03, 1, 0.95])  


plt.show()