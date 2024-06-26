# Mechanics-Informed Autoencoder Enables Automated Detection and Localization of Unforeseen Structural Damage [[arXiv]](https://arxiv.org/abs/2402.15492)

```BibTex
@article{li2024mechanics,
  title={Mechanics-Informed Autoencoder Enables Automated Detection and Localization of Unforeseen Structural Damage},
  author={Li, Xuyang and Bolandi, Hamed and Masmoudi, Mahdi and Salem, Talal and Lajnef, Nizar and Boddeti, Vishnu Naresh},
  journal={arXiv preprint arXiv:2402.15492},
  year={2024}
}
```

## Overview
In this work, we propose Mechanics-AE, a real-time SHM framework for automated damage detection and localization based on anomaly detection.

![Automated structural damage detection and localization framework](assets/fig1.png " ")

We train Mechanics-AE on a representative dataset of normal service structural operation response and efficiently reduce the raw sensor data stream for network training. The properties of damage are unknown/undefined during training. Once trained, the reconstruction errors between the network's input and output are used to construct a model reference representing the intact structural pattern. Data collected from the damaged structure are tested in the trained model. In the top right section of the figure, the observable shift in reconstruction errors effectively highlights the detection of anomalies indicative of damage. The incorporated mechanics knowledge notably enhances the distribution shift, leading to significant improvements in damage detection rate and the potential for early damage detection. In the bottom right section, we performed sensor-wise error comparisons based on norm value and displayed it in a contour. This process assists in early localization of anomalies representing the onset of damage.

### Damage detection
Mechanics-AE outperforms standard autoencoder in detecting different damage sizes across all metrics and can detect damages earlier.
![ ](assets/fig2.1.png " ")

Mechanics-AE also performs better than other machine learning methods, represented by 3 typical crack sizes.
![ ](assets/fig2.2.png " ")

### Damage localization
Mechanics-AE can localize much smaller damages, which is represented by achieving a higher damage localization rate as damage propagates.
![ ](assets/fig3.png " ")


### Run the model

```bash
git clone https://github.com/human-analysis/anamoly-detection-shm
cd anamoly-detection-shm
python main.py -e crack
```

There are 3 scenarios conducted: FEM simulations ('simu') and two experimental works ('crack' and 'bc') representing the crack and boundary condition variations. The trained model is provided in _saved_models_. By executing the code for different scenarios, the corresponding results (damage detection and localization figures) in the article are generated in the _figs_ folder. 

### Requirements
A `requirements.txt` file has been provided.


