# NOTES
These are the notes taken through the Entire Competition.

***NOTE:*** *Since, the data was not that much, we tested it on entire train data, testing different settings. When dealing with large data, it is always recommed to generate a smaller version of your dataset to run the experiments.*

**Training Session 1**
- LR = 10e^-5
- epochs = 20,000
- Last Training Score = 0.10224740207195282
- Last Testing Score = 0.18693949282169342

**Training Session 2**
- LR = 10e^-5
- epochs = 10,000
- Last Training Score = 11.864587783813477
- Last Testing Score = 11.752283096313477

**Training Session 3**
- LR = 10e^-4
- epochs = 10,000
- Last Training Score = 0.10457813739776611
- Last Testing Score = 0.17314718663692474

**Training Session 4**
- LR = 10e^-4
- epochs = 20,000
- Last Training Score = 0.10512429475784302
- Last Testing Score = 0.17610423266887665

**Conclusion 1:**
*As the number of epochs increases we need to reduce the learning rate for maximum efficiency.*

**Training Session 5**
- LR = 10e^-5
- epochs = 30,000
- Last Training Score = 0.07124461978673935
- Last Testing Score = 0.2052406519651413

**Conclusion 2:**
*As the number of epochs increases the model experiences **overfitting**.*

**Training Session 6**
- LR = 10e^-6
- epochs = 30,000
- Last Training Score = 0.12762823700904846
- Last Testing Score = 0.1820656955242157

The above training were done on the following neural network.
```python
class House_Price_Model_V0(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self.layer_0 = nn.Linear(in_features=79, out_features=128)
        self.layer_1 = nn.Linear(in_features=128, out_features=256)
        self.layer_2 = nn.Linear(in_features=256, out_features=128)
        self.layer_3 = nn.Linear(in_features=128, out_features=64)
        self.layer_4 = nn.Linear(in_features=64, out_features=32)
        self.layer_5 = nn.Linear(in_features=32, out_features=16)
        self.layer_6 = nn.Linear(in_features=16, out_features=4)
        self.layer_7 = nn.Linear(in_features=4, out_features=2)
        self.layer_8 = nn.Linear(in_features=2, out_features=1)
        
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.layer_0(x))
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        x = self.relu(self.layer_3(x))
        x = self.relu(self.layer_4(x))
        x = self.relu(self.layer_5(x))
        x = self.relu(self.layer_6(x))
        x = self.relu(self.layer_7(x))
        x = self.layer_8(x)

        return x
```

**Using Tree**

**Training Session 1:**
- Tree: DecisionTreeClassifier
- criterion: log_loss
- Test Size: 0.2
- Train Score: 0
- Test Score: 0.24631870135039244

**Training Session 2:**
- Tree: DecisionTreeRegressor
- criterion: squared_error
- Test Size: 0.2
- Train Score: 0
- Test Score: 0.2144613053565288

**Training Session 3:**
- Tree: DecisionTreeRegressor
- criterion: squared_error
- Test Size: 0.1
- Train Score: 0
- Test Score: 0.20250220946259068

**Training Session 4:**
- Tree: RandomForestClassifier
- criterion: log_loss
- Test Size: 0.2
- Train Score: 0
- Test Score: 0.20907006709580897

**Training Session 5:**
- Tree: RandomForestRegressor
- criterion: squared_error
- Test Size: 0.2
- Train Score: 0.05930344218501466
- Test Score: 0.15333684307739354

**Training Session 6:**
- Tree: RandomForestRegressor
- criterion: absolute_error
- Test Size: 0.2
- Train Score: 0.06059157714483402
- Test Score: 0.15136182072501175

**Training Session 7:**
- Tree: RandomForestRegressor
- criterion: friedman_mse
- Test Size: 0.2
- Train Score: 0.05932736144349766
- Test Score: 0.1533776449017082

**Training Session 8:**
- Tree: RandomForestRegressor
- criterion: poisson
- Test Size: 0.2
- Train Score: 0.058533578689850374
- Test Score: 0.15072496880084046
- Submission Score: 0.14999

**Training Session 9:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 200
- Test Size: 0.2
- Train Score: 0.058341566575136616
- Test Score: 0.15268412606848766

**Training Session 10:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 1000
- Test Size: 0.2
- Train Score: 0.058473014706075785
- Test Score: 0.1516478088620166

**Training Session 11:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 10_000
- Test Size: 0.2
- Training Time: 2m 0.4s
- Train Score: 0.0581243466475119
- Test Score: 0.15132087077263448
- Submission Score: **0.14816**

**Training Session 12:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 100
- min_samples_split: 79
- Test Size: 0.2
- Train Score: 0.15376311953638214
- Test Score: 0.1846085062330501

**Training Session 13:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 10_000
- min_samples_split: 79
- Test Size: 0.2
- Train Score: 0.15327577351573124
- Test Score: 0.18351926498801996

**Training Session 14:**
- Tree: RandomForestRegressor
- criterion: squared_error
- n_estimator: 1000
- oob_score: True
- Test Size: 0.2
- Train Score: 0.058473014706075785
- Test Score: 0.1516478088620166

**Training Session 15:**
- Tree: GradientBoostingClassifier
- criterion: squared_error
- loss: log_loss
- learning_rate: 0.1
- Test Size: 0.2
- Training Time: 10 min (approx.)
- Train Score: 0.052867035353972865
- Test Score: 0.349873027059346

**Training Session 16:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 100
- Test Size: 0.2
- Training Time: 0s
- Train Score: 0.08448995487007199
- Test Score: 0.14355652837833002
- Submission Score: **0.14052**

**Training Session 17:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.001
- n_estimator: 10_000
- Test Size: 0.2
- Training Time: 43s
- Train Score: 0.08413376949793494
- Test Score: 0.13965661774950228
- Submission Score: **0.13978**

**Training Session 17:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.0001
- n_estimator: 100_000
- Test Size: 0.2
- Training Time: 6m 59.5s
- Train Score: 0.08403201759971402
- Test Score: 0.13972577454415008

**Training Session 18:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.0001
- n_estimator: 10_00_000
- Test Size: 0.2
- Training Time: 70min 59s
- Train Score: 0.019812756573592726
- Test Score: 0.13723121400731605

**Training Session 19:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.01
- n_estimator: 100_000
- Test Size: 0.2
- Train Score: 1.3776197040953571e-06
- Test Score: 0.13957636302864856

**Training Session 20:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 1
- n_estimator: 1000
- Test Size: 0.2
- Train Score: 4.3150793371019827e-07
- Test Score: 0.19578175091518948

**Training Session 21:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 1
- n_estimator: 100
- Test Size: 0.2
- Train Score: 0.03136736618805258
- Test Score: 0.19614246610943395

**Training Session 22:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 10_000
- Test Size: 0.2
- Train Score: 7.617169510367186e-07
- Test Score: 0.14053228347191932

**Training Session 23:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 79
- Test Size: 0.1
- Train Score: 0.09504109216246273
- Test Score: 0.11798030400834812
- **Submission Score:**: 0.1402

**Training Session 24:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.09125975953169842
- Test Score: 0.1440780263099032

**Training Session 25:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.5
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.04787690958388537
- Test Score: 0.16513552336589804
- **Submission Score:**: 0.15797

**Training Session 26:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.05
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.11753411995977586
- Test Score: 0.1562763803084833

**Training Session 27:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.01
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.2571311915929385
- Test Score: 0.2952115322761898

**Training Session 28:**
- Tree: DecisionTreeClassifier
- criterion: log_loss
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.2571311915929385
- Test Score: 0.2952115322761898

**Training Session 29:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.0001
- n_estimator: 100_000
- Test Size: 0.2
- Train Score: 0.08403201759971402
- Test Score: 0.13972577454415008
- Training Time: 7m 12.5s
- **Submission Score:** 0.13963

**Training Session 30:**
- Tree: GradientBoostingRegressor
- criterion: friedman_mse
- loss: huber
- learning_rate: 0.1
- n_estimator: 100
- Test Size: 0.2
- Train Score: 0.08810653192492615
- Test Score: 0.13883723872904982
- Training Time: 0s
- **Submission Score:** 0.1408

**Training Session 31:**
- Tree: GradientBoostingRegressor
- criterion: friedman_mse
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 100
- Test Size: 0.2
- Train Score: 0.08448995487007199
- Test Score: 0.14355652837833002
- Training Time: 0s

**Training Session 32:**
- Tree: GradientBoostingRegressor
- criterion: friedman_mse
- loss: squared_error
- learning_rate: 0.1
- n_estimator: 79
- Test Size: 0.2
- Train Score: 0.08448995487007199
- Test Score: 0.14355652837833002
- Training Time: 0s

**Training Session 33:**
- Tree: GradientBoostingRegressor
- criterion: squared_error
- loss: squared_error
- learning_rate: 0.0001
- n_estimator: 100_000
- Test Size: 0.2
- Train Score: 
- Test Score: 
- Training Time: 
- **Submission Score:** 