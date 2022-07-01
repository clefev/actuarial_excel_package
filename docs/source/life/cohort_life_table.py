def cohort_force_of_mortality(x, t, table=""):
    r"""
    Compute the force of mortality :math:`\mu_x(t)`.

    Note
    ----
    The force of mortality :math:`\mu_x(t)` represents the instantaneous rate of mortality at age :math:`x` in calendar year :math:`t`.
    It should be noted that the force of mortality is always positive (and can even be greater than 1) i.e. :math:`\mu_x(t) \geq 0`.

    From a probabilistic point of view, the force of mortality is defined as

    .. math::
        \mu_x(t) = \lim_{\tau \to 0} \frac{Pr \left( x < T(t-x) \leq x+\tau \mid T(t-x) > x \right)}{\tau}

    where :math:`T(t)` is the random variable describing the time-to-death (lifetime) of a newborn born in year :math:`t`.

    The force of mortality can be used to calculate any survival probabilities:

    .. math::
        _np_x(t) = e^{-\int_0^n \mu_{x+\tau}(t+\tau) d\tau}.

    As life tables are given only for integer ages and integer calendar years, we assume that the force of mortality is constant
    between two consecutive integer ages and calendar years that is

    .. math::
        \mu_{x+\xi}(t+\tau) = \mu_x(t)

    for all :math:`(x,t) \in \mathbb{N}^2` and :math:`(\xi,\tau) \in [0,1)^2`.

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    table : string
        Life table to use.

    Returns
    -------
    numeric (non-negative)
        Force of mortality of an individual aged :math:`x` in calendar year :math:`t`.

    Examples
    --------
    Compute :math:`\mu_{50}(2030)` according to the IABE table for males
    (force of mortality of a 50-year-old Belgian male in the calendar year 2030):

    >>> cohort_force_of_mortality(50, 2030, "IABE male")
    0.002287

    Because we assume that the force of mortality is constant by age and calendar year, this is the same as
    :math:`\mu_{50.3}(2030)`, :math:`\mu_{50}(2030.8)` or :math:`\mu_{50.87}(2030.46)` for example:

    >>> cohort_force_of_mortality(50.3, 2030, "IABE male")
    0.002287
    >>> cohort_force_of_mortality(50, 2030.8, "IABE male")
    0.002287
    >>> cohort_force_of_mortality(50.87, 2030.46, "IABE male")
    0.002287

    But this is different from :math:`\mu_{51}(2030)` or :math:`\mu_{50}(2031)` because a new integer age or calendar year
    implies a new force of mortality assumption:

    >>> cohort_force_of_mortality(51, 2030, "IABE male")
    0.002678
    >>> cohort_force_of_mortality(50, 2031, "IABE male")
    0.002252
    """

    pass

def cohort_survival_probability(x, t, n=1, table=""):
    r"""
    Compute the survival probability :math:`_np_x(t)`.

    Note
    ----
    The survival probability :math:`_np_x(t)` is the probability that an individual
    aged :math:`x` in calendar year :math:`t` survives in the next :math:`n` years.
    It is computed as

    .. math::
        _np_x(t) = e^{-\int_0^n \mu_{x+\tau}(t+\tau) d\tau}

    where :math:`\mu_x(t)` is the force of mortality of an individual aged :math:`x` in calendar year :math:`t`.

    From a probabilistic point of view, :math:`_np_x(t)` is the survival function of
    the random variable :math:`T_x(t)` that is

    .. math::
        _np_x(t) = Pr \left( T_x(t) > n \right) = Pr \left( T(t-x) > x+n \mid T(t-x) > x \right)

    where :math:`T_x(t)` is the random variable describing the remaining lifetime of an individual aged :math:`x` in calendar year :math:`t`.

    Finally, note that we have the following decomposition formula

    .. math::
        _np_x(t) = {}_{\tau}p_x(t) \cdot {}_{n-\tau}p_{x+\tau}(t+\tau)

    for all :math:`\tau \in (0,n)`.

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    n : numeric
        Horizon time.
    table : string
        Life table to use.

    Returns
    -------
    numeric (between 0 and 1)
        Probability that an individual aged :math:`x` in calendar year :math:`t` survives in the next :math:`n` years.

    Examples
    --------
    Compute :math:`p_{50}(2030)` according to the IABE table for males
    (probability that a Belgian man aged 50 in the calendar year 2030 will survive the following year):

    >>> cohort_survival_probability(50, 2030, 1, "IABE male")
    99.77%

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_survival_probability(50, 2060, 1, "IABE male")
    99.86%

    Compute :math:`_{10.5}p_{54.5}(2030.75)` according to the IABE table for females:

    >>> cohort_survival_probability(54.5, 2030.75, 10.5, "IABE female")
    96.01%
    """

    pass

def cohort_death_probability(x, t, n=1, table=""):
    r"""
    Compute the death probability :math:`_nq_x(t)`.

    Note
    ----
    The death probability :math:`_nq_x(t)` is the probability that an individual
    aged :math:`x` in calendar year :math:`t` dies in the next :math:`n` years.
    It is computed as

    .. math::
        _nq_x(t) = 1 - {}_np_x(t) = 1 - e^{-\int_0^n \mu_{x+\tau}(t+\tau) d\tau}

    where :math:`\mu_x(t)` is the force of mortality of an individual aged :math:`x` in calendar year :math:`t`.

    From a probabilistic point of view, :math:`_nq_x(t)` is the cumulative distribution function (cdf) of
    the random variable :math:`T_x(t)` that is

    .. math::
        _nq_x(t) = Pr \left( T_x(t) \leq n \right) = Pr \left( T(t-x) \leq x+n \mid T(t-x) > x \right)

    where :math:`T_x(t)` is the random variable describing the remaining lifetime of an individual aged :math:`x` in calendar year :math:`t`.

    Finally, note that we have the following decomposition formula

    .. math::
        _nq_x(t) = {}_{\tau}q_x(t) + {}_{\tau}p_x(t) \cdot {}_{n-\tau}q_{x+\tau}(t+\tau)

    for all :math:`\tau \in (0,n)`.

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    n : numeric
        Horizon time.
    table : string
        Life table to use.

    Returns
    -------
    numeric (between 0 and 1)
        Probability that an individual aged :math:`x` in calendar year :math:`t` dies in the next :math:`n` years.

    Examples
    --------
    Compute :math:`q_{50}(2030)` according to the IABE table for males
    (probability that a Belgian man aged 50 in the calendar year 2030 will die the following year):

    >>> cohort_death_probability(50, 2030, 1, "IABE male")
    0.23%

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_death_probability(50, 2060, 1, "IABE male")
    0.14%

    Compute :math:`_{10.5}q_{54.5}(2030.75)` according to the IABE table for females:

    >>> cohort_death_probability(54.5, 2030.75, 10.5, "IABE female")
    3.99%
    """

    pass

def cohort_life_expectancy(x, t, table=""):
    r"""
    Compute the life expectancy :math:`e_x(t)`.

    Note
    ----
    The life expectancy :math:`e_x(t)` is the expected remaining lifetime of an individual aged :math:`x` in calendar year :math:`t`.
    It is defined by

    .. math::
        e_x(t) = \mathbb{E}[T_x(t)] = \int_0^\infty {}_{\tau}p_x(t) d\tau

    where :math:`T_x(t)` is the random variable describing the remaining lifetime of an individual aged :math:`x` in calendar year :math:`t`.

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    table : string
        Life table to use.

    Returns
    -------
    numeric (non-negative)
        Life expectancy of an individual aged :math:`x` in calendar year :math:`t`.

    Examples
    --------
    Compute :math:`e_{65}(2030)` according to the IABE table for males
    (life expectancy of a Belgian male aged 65 in the calendar year 2030):

    >>> cohort_life_expectancy(65, 2030, "IABE male")
    21.71

    Compare with a male aged 65 in the calendar year 2060:

    >>> cohort_life_expectancy(65, 2060, "IABE male")
    25.11

    Compare the results with the female table:

    >>> cohort_life_expectancy(65, 2030, "IABE female")
    24.16
    >>> cohort_life_expectancy(65, 2060, "IABE female")
    26.74
    """

    pass

def cohort_pure_endowment(x, t, n=1, i=0, table=""):
    r"""
    Compute the present value of a pure endowment :math:`_nE_x(t)`.

    Note
    ----
    A pure endowment consists of paying an amount of 1 unit in :math:`n` years from now
    to an individual currently aged :math:`x` in calendar year :math:`t` if the individual survives.

    The present value is computed as

    .. math::
        _nE_x(t) = \frac{_np_x(t)}{(1+i)^n}

    where :math:`_np_x(t)` is the probability that an individual aged :math:`x` in calendar year :math:`t` survives in the
    next :math:`n` years and :math:`i` is the guaranteed interest rate.

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.

    Returns
    -------
    numeric (non-negative)
        Present value of the pure endowment.

    Examples
    --------
    Compute :math:`E_{50}(2030)` according to the IABE table for males with :math:`i=2\%`:

    >>> cohort_pure_endowment(50, 2030, 1, 0.02, "IABE male")
    0.9782

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_pure_endowment(50, 2060, 1, 0.02, "IABE male")
    0.9790

    Compute :math:`_{10.5}E_{54.5}(2030.75)` according to the IABE table for females with :math:`i=2\%`:

    >>> cohort_pure_endowment(54.5, 2030.75, 10.5, 0.02, "IABE female")
    0.7799

    Finally, note that by definition the calculation of a pure endowment amounts exactly to discounting
    a survival probability. For example, the result of the example above can be obtained as follows:

    >>> cohort_survival_probability(54.5, 2030.75, 10.5, "IABE female") / (1 + 0.02)^10.5
    0.7799
    """

    pass

def cohort_whole_life_annuity(x, t, i=0, table="", beginning=False, freq=1):
    r"""
    Compute the present value of a whole life annuity :math:`a_x(t)`.

    Note
    ----
    A whole life annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` in calendar year :math:`t` is alive.

    If the payment frequency is annual, the present value is given by

    .. math::
        a_x(t) = \sum_{k \geq 1} {}_kE_x(t) = \frac{p_x(t)}{1+i} + \frac{_2p_x(t)}{(1+i)^2} + ...

    in the case of payments at the end of the year, or

    .. math::
        \ddot{a}_x(t) = \sum_{k \geq 0} {}_kE_x(t) = 1 + \frac{p_x(t)}{1+i} + \frac{_2p_x(t)}{(1+i)^2} + ...
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        a_x^{(m)}(t) = \sum_{k \geq 1} {}_{\frac{k}{m}}E_x(t) \qquad \text{and} \qquad \ddot{a}_x^{(m)}(t) = \sum_{k \geq 0} {}_{\frac{k}{m}}E_x(t)

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or :math:`m=4` for quarterly payments).

    Finally, we have the following relations:

    .. math::
        \ddot{a}_x(t) = 1 + a_x(t) \qquad \text{and} \qquad a_x(t) = {}_na_x(t) + {}_nE_x(t) \cdot a_{x+n}(t+n).

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    beginning : bool
        Indicate whether the payments occur at the beginning of the period.
        The default assumes end of period payments.
    freq : numeric
        Payment frequency: number of payments per year.
        The default assumes annual payment.

    Returns
    -------
    numeric (non-negative)
        Present value of the whole life annuity.

    Examples
    --------
    Compute :math:`a_{50}(2030)` and :math:`\ddot{a}_{50}(2030)` according to the IABE table for males with :math:`i=2\%`
    (the annuity is paid on a yearly basis):

    >>> cohort_whole_life_annuity(50, 2030, 0.02, "IABE male")
    24.89
    >>> cohort_whole_life_annuity(50, 2030, 0.02, "IABE male", TRUE)
    25.89

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_whole_life_annuity(50, 2060, 0.02, "IABE male")
    26.75
    >>> cohort_whole_life_annuity(50, 2060, 0.02, "IABE male", TRUE)
    27.75

    Compute :math:`a_{54.5}^{(4)}(2030.75)` and :math:`\ddot{a}_{54.5}^{(4)}(2030.75)` according to the IABE table for females with :math:`i=2\%`
    (the annuity is paid on a quarterly basis):

    >>> cohort_whole_life_annuity(54.5, 2030.75, 0.02, "IABE female",,4)
    97.35
    >>> cohort_whole_life_annuity(54.5, 2030.75, 0.02, "IABE female", TRUE, 4)
    98.35
    """

    pass

def cohort_term_annuity(x, t, n=1, i=0, table="", beginning=False, freq=1):
    r"""
    Compute the present value of a term annuity :math:`_na_x(t)`.

    Note
    ----
    A term annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` in calendar year :math:`t` is alive and with a maximum payment period of :math:`n` years.

    If the payment frequency is annual, the present value is given by

    .. math::
        _na_x(t) = \sum_{k=1}^n {}_kE_x(t) = \frac{p_x(t)}{1+i} + \frac{_2p_x(t)}{(1+i)^2} + ... + \frac{_np_x(t)}{(1+i)^n}

    in the case of payments at the end of the year, or

    .. math::
        _n\ddot{a}_x(t) = \sum_{k=0}^{n-1} {}_kE_x(t) = 1 + \frac{p_x(t)}{1+i} + \frac{_2p_x(t)}{(1+i)^2} + ... + \frac{_{n-1}p_x(t)}{(1+i)^{n-1}}
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        _na_x^{(m)}(t) = \sum_{k=1}^{n \cdot m} {}_{\frac{k}{m}}E_x(t) \qquad \text{and} \qquad _n\ddot{a}_x^{(m)}(t) = \sum_{k=0}^{n \cdot m - 1} {}_{\frac{k}{m}}E_x(t)

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or :math:`m=4` for quarterly payments).

    Finally, we have the following relations:

    .. math::
        _n\ddot{a}_x(t) = 1 + {}_{n-1}a_x(t) \qquad \text{and} \qquad _n\ddot{a}_x^{(m)}(t) = 1 + {}_{n-\frac{1}{m}}a_x^{(m)}(t).

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    beginning : bool
        Indicate whether the payments occur at the beginning of the period.
        The default assumes end of period payments.
    freq : numeric
        Payment frequency: number of payments per year.
        The default assumes annual payment.

    Returns
    -------
    numeric (non-negative)
        Present value of the term annuity.

    Examples
    --------
    Compute :math:`_{10}a_{50}(2030)` and :math:`_{10}\ddot{a}_{50}(2030)` according to the IABE table for males with :math:`i=2\%`
    (the annuity is paid on a yearly basis):

    >>> cohort_term_annuity(50, 2030, 10, 0.02, "IABE male")
    8.83
    >>> cohort_term_annuity(50, 2030, 10, 0.02, "IABE male", TRUE)
    9.04

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_term_annuity(50, 2060, 10, 0.02, "IABE male")
    8.89
    >>> cohort_term_annuity(50, 2060, 10, 0.02, "IABE male", TRUE)
    9.09

    Compute :math:`_{10.5}a_{54.5}^{(4)}(2030.75)` and :math:`_{10.5}\ddot{a}_{54.5}^{(4)}(2030.75)` according to the IABE table for females with :math:`i=2\%`
    (the annuity is paid on a quarterly basis):

    >>> cohort_term_annuity(54.5, 2030.75, 10.5, 0.02, "IABE female",,4)
    37.16
    >>> cohort_term_annuity(54.5, 2030.75, 10.5, 0.02, "IABE female", TRUE, 4)
    37.38
    """

    pass

def cohort_whole_life_insurance(x, t, i=0, table="", freq=1):
    r"""
    Compute the present value of a whole life insurance :math:`\bar{A}_x(t)`.

    Note
    ----
    A whole life insurance consists of paying an amount of 1 unit when an individual aged :math:`x` in calendar year :math:`t` dies.
    The formula assumes that the payment occurs at the middle of the period and not at the exact date of the death.

    If the period frequency is annual, the present value is given by

    .. math::
        \begin{align}
            \bar{A}_x(t) &= \sum_{k \geq 0} \frac{_kp_x(t) \cdot q_{x+k}(t+k)}{(1+i)^{k+0.5}} \\
            &= \frac{q_x(t)}{(1+i)^{0.5}} + \frac{p_x(t) \cdot q_{x+1}(t+1)}{(1+i)^{1.5}} + \frac{_2p_x(t) \cdot q_{x+2}(t+2)}{(1+i)^{2.5}} + ...
        \end{align}

    If the period frequency is split (e.g., monthly period), the present value is given by

    .. math::
        \bar{A}_x^{(m)}(t) = \sum_{k \geq 0} \frac{_\frac{k}{m}p_x(t) \cdot {}_{\frac{1}{m}}q_{x+\frac{k}{m}}(t+\frac{k}{m})}{(1+i)^{\frac{k+0.5}{m}}}

    where :math:`m` is the period frequency (e.g., :math:`m=12` for monthly period or :math:`m=4` for quarterly period).

    Finally, we have the following relation:

    .. math::
        \bar{A}_x(t) = {}_n\bar{A}_x(t) + {}_nE_x(t) \cdot \bar{A}_{x+n}(t+n).

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    freq : numeric
        Period frequency.
        The default assumes annual period.

    Returns
    -------
    numeric (non-negative)
        Present value of the whole life insurance.

    Examples
    --------
    Compute :math:`\bar{A}_{50}(2030)` according to the IABE table for males with :math:`i=2\%`
    (the death benefit is paid at the middle of the year of the death):

    >>> cohort_whole_life_insurance(50, 2030, 0.02, "IABE male")
    0.4972

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_whole_life_insurance(50, 2060, 0.02, "IABE male")
    0.4604

    Compute :math:`\bar{A}_{54.5}^{(4)}(2030.75)` according to the IABE table for females with :math:`i=2\%`
    (the death benefit is paid at the middle of the quarter of the death):

    >>> cohort_whole_life_insurance(54.5, 2030.75, 0.02, "IABE female", 4)
    0.5156
    """

    pass

def cohort_term_insurance(x, t, n=1, i=0, table="", freq=1):
    r"""
    Compute the present value of a term insurance :math:`_n\bar{A}_x(t)`.

    Note
    ----
    A term insurance consists of paying an amount of 1 unit when an individual aged :math:`x` in calendar year :math:`t` dies in the next :math:`n` years.
    The formula assumes that the payment occurs at the middle of the period and not at the exact date of the death.

    If the period frequency is annual, the present value is given by

    .. math::
        \begin{align}
            _n\bar{A}_x(t) &= \sum_{k=0}^{n-1} \frac{_kp_x(t) \cdot q_{x+k}(t+k)}{(1+i)^{k+0.5}} \\
            &= \frac{q_x(t)}{(1+i)^{0.5}} + \frac{p_x(t) \cdot q_{x+1}(t+1)}{(1+i)^{1.5}} + ... + \frac{_{n-1}p_x(t) \cdot q_{x+n-1}(t+n-1)}{(1+i)^{n-0.5}}.
        \end{align}

    If the period frequency is split (e.g., monthly period), the present value is given by

    .. math::
        _n\bar{A}_x^{(m)}(t) = \sum_{k=0}^{n \cdot m - 1} \frac{_\frac{k}{m}p_x(t) \cdot {}_{\frac{1}{m}}q_{x+\frac{k}{m}}(t+\frac{k}{m})}{(1+i)^{\frac{k+0.5}{m}}}

    where :math:`m` is the period frequency (e.g., :math:`m=12` for monthly period or :math:`m=4` for quarterly period).

    Parameters
    ----------
    x : numeric
        Age.
    t : numeric
        Calendar year.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    freq : numeric
        Period frequency.
        The default assumes annual period.

    Returns
    -------
    numeric (non-negative)
        Present value of the term insurance.

    Examples
    --------
    Compute :math:`_{10}\bar{A}_{50}(2030)` according to the IABE table for males with :math:`i=2\%`
    (the death benefit is paid at the middle of the year of the death):

    >>> cohort_term_insurance(50, 2030, 10, 0.02, "IABE male")
    0.0318

    Compare with a male aged 50 in the calendar year 2060:

    >>> cohort_term_insurance(50, 2060, 10, 0.02, "IABE male")
    0.0195

    Compute :math:`_{10.5}\bar{A}_{54.5}^{(4)}(2030.75)` according to the IABE table for females with :math:`i=2\%`
    (the death benefit is paid at the middle of the quarter of the death):

    >>> cohort_term_insurance(54.5, 2030.75, 10.5, 0.02, "IABE female", 4)
    0.0356
    """

    pass