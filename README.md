# AB_testing
We want to  measure if changing the website's background color leads to an increase of the time visitors spend on it. Rewriting this as hypothesis test, the **null hypothesis** is that the change did not affect the time a visitor spend. Let's name the variables:

- $\mu_c$ is the average time a user **in the control group** spend in the website. Recall that the **control group** is the group accessing the website without the change in the background color.
- $\mu_v$ is the average time a user **in the variation groups** spend in the website. Recall that the **variation group** is the groups accessing the website **with the updated background color**.

Our intention is to measure if the background color leads to an **increase** in the time a visitor spend in the website. So writing this experiment as a hypothesis test, the **null hypothesis** is then $H_0: \mu_c = \mu_v$ and the **alternative hypothesis** is $H_1: \mu_v > \mu_c$, or equivalently, $H_1: \mu_v - \mu_c > 0$. 

Therefore, the hypothesis you will test is:

$$H_0: \mu_v = \mu_c \quad \text{vs.} \quad H_1: \mu_v - \mu_c > 0$$

This is a **right-tailed** test, as we are looking for an increase in the average time. We have more than 2000 users per group, this is a great amount of data so it is reasonable to rely in the Central Limit Theorem that the **average time** for each group follows a normal distribution. This result is for the group **average time** altogether and not that the time each user spend follows a normal distribution. We don't know the exact distribution for the amount of time a user spend in your website, however, the CLT assures that if we gather enough data, their average time will be very close to a normal distribution whose mean is the average time a user spend in the website. Let's then define two new quantities:

- $\overline{X}_c$ - the control group **sample mean**.
- $\overline{X}_v$ - the variation group **sample mean**.
- $n_c$ - the control group **size**.
- $n_v$ - the variation group **size**.

So, by the Central Limit Theorem, we may suppose that

- $$\overline{X}_c \sim N\left(\mu_c, \left(\frac{\sigma_c}{\sqrt{n_c}}\right)^2\right)$$
- $$\overline{X}_v \sim N\left(\mu_v, \left(\frac{\sigma_v}{\sqrt{n_v}}\right)^2\right)$$

With our assumptions of normality, $\overline{X}_v - \overline{X}_c$ also follows a normal distribution. So, if $H_0$ is true, then $\mu_c = \mu_v$ and $\mu_v - \mu_c = 0$, therefore:

$$\overline{X}_c - \overline{X}_v \sim N\left(\mu_v - \mu_c, \left(\dfrac{\sigma_v}{\sqrt{n_v}}\right)^2 + \left(\dfrac{\sigma_c}{\sqrt{n_c}}\right)^2\right) = N\left(0, \left(\dfrac{\sigma_v}{\sqrt{n_v}}\right)^2 + \left(\dfrac{\sigma_c}{\sqrt{n_c}}\right)^2\right)$$

Or, equivalently:

$$\frac{\left( \overline{X}_v - \overline{X}_c \right)}{\sqrt{\left(\frac{\sigma_v}{\sqrt{n_v}}\right)^2 + \left(\frac{\sigma_c}{\sqrt{n_c}}\right)^2}} \sim N(0, 1)$$

However,  **we don't know the exact values for** $\sigma_v$ and $\sigma_c$, as they are the **population standard deviation** and we are working with a sample, so the best we can do is compute the **sample standard deviation**. We must replace $\sigma_c$ and $\sigma_v$ by the sample standard deviation, respectively, $s_c$ and $s_v$. This changes the random variable from a Normal to a t-student:

$$t = \frac{\left( \overline{X}_v - \overline{X}_c \right)}{\sqrt{\left(\frac{s_v}{\sqrt{n_v}}\right)^2 + \left(\frac{s_c}{\sqrt{n_c}}\right)^2}} \sim t_d$$

Where $d$ is the **degrees of freedom** for this scenario. If we suppose that both groups have the same standard deviation, then $d = n_c + n_v - 2$, however there is no argument supporting this supposition, so the formula for the degrees of freedom gets a bit messier:

$$d = \frac{\left[\frac{s_{v}^2}{n_v} + \frac{s_{c}^2}{n_c} \right]^2}{\frac{(s_{v}^2/n_v)^2}{n_v-1} + \frac{(s_{c}^2/n_c)^2}{n_c-1}}$$

Once we get the actual value for $t_d$ the, with a given significance level $\alpha$, we can decide if this value falls within the range of values that are likely to occur in the $t$-student distribution (where 'likely' is related with our significance level). To perform this step we must find the value $p$ such that 

$$p = P(t_d > t | H_0)$$

If this value is less than our significance level $\alpha$, then we **reject the null hypothesis**, because it means that we observed a value that is very unlikely to occur (unlikely here means that is less than the significance level we have set) if $H_0$ is true.

The $P(t_d \leq t)$ is the $\text{CDF}$ (cumulative distribution function) for the $t$-student distribution with $d$ degrees of freedom in the point $x = t$, so to compute $P(t_d > t)$ we may compute:

$$P(t_d > t) = 1 - \text{CDF}_{t_d}(t)$$

Since $P(t_d \leq t) + P(t_d > t) = 1$
