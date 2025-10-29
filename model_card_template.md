# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

**Developer**: Adityasai Pakki / WGU

**Model type**: Random Forest Classifier

**Contact Information**: Please contact [apakki@wgu.edu](mailto://apakki@wgu.edu) for any questions or feedback.

**License**: This model is licensed under the **MIT LICENSE**. See bottom of this page for details.

## Intended Use

**Primary Intended Use**: This model is trained on cenus data of over 25k adults to determine whether or not someone has over a $50K USD income based on demographic and occupational features.

**Primary intended users**: This model was developed as an educational tool and is intended for Data Scientists, Researchers, and Students to use as a technical model.

**Out-of-scope Uses**: This model should NOT be used as way to determine fair wages or otherwise discriminate against people of certain backgrounds. Ideally, this model should not be used in any high-stakes decision making, especially out of an academic context.

## Training Data

This model was trained on a multivariate dataset provided by UC Irvine sourced from the 1994 United States Census Buereau's database. The data consists of various demographic, educational, financial, and occupational data which is then used to predict the expected income of a person. As of writing, this data is nearly 31 years old and therefore may include societal biases and factors that have changed over the decades.

The data was cleaned manually and then pre-processed for the ML pipeline. Data points withs missing values were discarded reduction of the size of our dataset from 48842 to 32561 - split between training and testing data.

`Size: 26049 x 14`

## Evaluation Data

The final dataset (found in `/data/census.csv`) was split into two groups each consisting of 80 and 20 percent respectively. The intial 80% of the data was used as training data while the remaing 20% became the evalutation data.

`Size: 6512  x 14`

## Metrics

3 Metrics were used to determine the performance of the model: _Precision, Recall, and F1._

### **Overall Metrics**

| Precision | Recall | F1     |
| --------- | ------ | ------ |
| 0.7391    | 0.6384 | 0.6851 |

Above are the overall metrics for our model across a wide array of demographic census data.

### **Slice-Based Metrics**

The full list of Slice based Metrics can be found in `slice_output.txt`. Below are a few samples.

| **EDUCATION** | Precision | Recall |   F1   |
| :-----------: | :-------: | :----: | :----: |
|    HS-grad    |  0.6460   | 0.4232 | 0.5114 |
|  Assoc-acdm   |  0.7105   | 0.5745 | 0.6353 |
|   Bachelors   |  0.7569   | 0.7333 | 0.7449 |
|   Doctorate   |  0.8500   | 0.8947 | 0.8718 |

> Assoc-acdm = Academic Associates rather than vocational.

| **MARITAL STATUS** | Precision | Recall |   F1   |
| :----------------: | :-------: | :----: | :----: |
|      Divorced      |  0.7778   | 0.3398 | 0.4730 |
|   Never-Married    |  0.8148   | 0.4272 | 0.5605 |

| **Sex** | Precision | Recall |   F1   |
| :-----: | :-------: | :----: | :----: |
|  Male   |  0.7410   | 0.6607 | 0.6985 |
| Female  |  0.7256   | 0.5107 | 0.5995 |

## Ethical Considerations

This model uses data that is completely public and does not contain any immediately identifiable information, especially being 30 years old. However, if miused this data does pose a risk of exacerbating prejudices and confirming pre-conceived biases. Caution should be taken against blindly using demographic data to determine someone's worth outside this academic context.

## Caveats and Recommendations

This model has not been adjusted for biases or optimized in any form. This classifier should not be used for anything other than educational purposes. Further, this data is over 3 decades old (1994) and is not indicative of past or current trends outside of the scope of that singular census.

We recommend training the model on more recent data as well as improving the training-test validation datasets.

> R. Kohavi. "Census Income," UCI Machine Learning Repository, 1996. [Online]. Available: https://doi.org/10.24432/C5GP7S.

<hr/>

```md
MIT License

Copyright (c) 2025 Adityasai Kushal Pakki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
