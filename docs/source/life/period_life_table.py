def survivors(x, table="XR", correction=0):
    r"""
    Compute the number of survivors :math:`l_x` according to the life table.

    Note
    ----
    The number of survivors at age :math:`x` is denoted by :math:`l_x`.

    If the age :math:`x` is given as an integer (e.g., :math:`x=50` for an individual aged 50 years old),
    then :math:`l_x` represents the number of people alive at age :math:`x` according to the life table.

    If the age :math:`x` is given as a decimal number (e.g., :math:`x=50.75` for an individual aged 50 years and 9 months),
    then :math:`l_x` is interpolated as following

    .. math::
        l_x = l_{\lfloor x \rfloor}^{1-\tau} \cdot l_{\lfloor x \rfloor + 1}^{\tau} = l_{\lfloor x \rfloor} \cdot p_{\lfloor x \rfloor}^\tau

    where the age :math:`x = \lfloor x \rfloor + \tau` is decomposed as an integer part and a decimal part
    (e.g., if :math:`x=50.75`, we have :math:`\lfloor x \rfloor = 50` and :math:`\tau=0.75`).

    The exponential interpolation assumes a constant force of mortality between two consecutive integer ages.

    Parameters
    ----------
    x : numeric
        Age.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (non-negative)
        Number of survivors.

    Examples
    --------
    Compute :math:`l_{50}`, :math:`l_{51}` and :math:`l_{50.75}` according to the MR table:

    >>> survivors(50, "MR")
    941 273
    >>> survivors(51, "MR")
    937 628
    >>> survivors(50.75, "MR")
    938 537.92 # 941 273^0.25 * 937 628^0.75 (exponential interpolation)

    Compute :math:`l_{65}` according to the XR table with an age correction of -5 years
    (this is equivalent to compute :math:`l_{60}` without age correction as shown below):

    >>> survivors(65, "XR", -5)
    916 308
    >>> survivors(60, "XR")
    916 308
    """

    pass

def deaths(x, n=1, table="XR", correction=0):
    r"""
    Compute the number of deaths between age :math:`x` and :math:`x+n` according to the life table.

    Note
    ----
    The number of deaths :math:`_nd_x` between age :math:`x` and :math:`x+n` is computed as

    .. math::
        _nd_x = l_x - l_{x+n}

    where :math:`l_x` is the number of people alive at age :math:`x`.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (non-negative)
        Number of deaths.

    Examples
    --------
    Compute :math:`d_{50}` according to the MR table:

    >>> deaths(50, 1, "MR")
    3 645

    Compute the number of deaths between age 54.5 and 65 according to the FK' table:

    >>> deaths(54.5, 10.5, "FK'")
    110 413.39

    Compute the number of deaths between age 80 and 85 according to the XR table with an age correction of -3 years:

    >>> deaths(80, 5, "XR", -3)
    137 040
    """

    pass

def survival_probability(x, n=1, table="XR", correction=0):
    r"""
    Compute the survival probability :math:`_np_x`.

    Note
    ----
    The survival probability :math:`_np_x` is the probability that an individual
    aged :math:`x` survives in the next :math:`n` years.
    It is computed as

    .. math::
        _np_x = \frac{l_{x+n}}{l_x}

    where :math:`l_x` is the number of people alive at age :math:`x`.

    From a probabilistic point of view, :math:`_np_x` is the survival function of
    the random variable :math:`T_x` that is

    .. math::
        {}_np_x = Pr \left( T_x > n \right) = Pr \left( T > x+n \mid T > x \right)

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Finally, note that we have the following decomposition formula

    .. math::
        _np_x = {}_{\tau}p_x \cdot {}_{n-\tau}p_{x+\tau}

    for all :math:`\tau \in (0,n)`.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (between 0 and 1)
        Probability that an individual aged :math:`x` survives in the next :math:`n` years.

    Examples
    --------
    Compute :math:`p_{50}` according to the MR table:

    >>> survival_probability(50, 1, "MR")
    99.61%

    Compute :math:`_{10.5}p_{54.5}` according to the FK' table:

    >>> survival_probability(54.5, 10.5, "FK'")
    87.89%

    Compute :math:`_{5}p_{80}` according to the XR table with an age correction of -3 years:

    >>> survival_probability(80, 5, "XR", -3)
    80.18%
    """

    pass

def death_probability(x, n=1, table="XR", correction=0):
    r"""
    Compute the death probability :math:`_nq_x`.

    Note
    ----
    The death probability :math:`_nq_x` is the probability that an individual
    aged :math:`x` dies in the next :math:`n` years.
    It is computed as

    .. math::
        _nq_x = 1 - _np_x = \frac{l_x - l_{x+n}}{l_x}

    where :math:`l_x` is the number of people alive at age :math:`x`.

    From a probabilistic point of view, :math:`_nq_x` is the cumulative distribution function (cdf) of
    the random variable :math:`T_x` that is

    .. math::
        _nq_x = Pr \left( T_x \leq n \right) = Pr \left( T \leq x+n \mid T > x \right)

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Finally, note that we have the following decomposition formula

    .. math::
        _nq_x = {}_{\tau}q_x + {}_{\tau}p_x \cdot {}_{n-\tau}q_{x+\tau}

    for all :math:`\tau \in (0,n)`.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (between 0 and 1)
        Probability that an individual aged :math:`x` dies in the next :math:`n` years.

    Examples
    --------
    Compute :math:`q_{50}` according to the MR table:

    >>> death_probability(50, 1, "MR")
    0.39%

    Compute :math:`_{10.5}q_{54.5}` according to the FK' table:

    >>> death_probability(54.5, 10.5, "FK'")
    12.11%

    Compute :math:`_{5}q_{80}` according to the XR table with an age correction of -3 years:

    >>> death_probability(80, 5, "XR", -3)
    19.82%
    """

    pass

def force_of_mortality(x, table="XR", correction=0):
    r"""
    Compute the force of mortality :math:`\mu_x`.

    Note
    ----
    The force of mortality :math:`\mu_x` represents the instantaneous rate of mortality at age :math:`x`
    (risk of dying at age :math:`x` being alive at this age).
    It should be noted that the force of mortality is always positive (and can even be greater than 1) i.e. :math:`\mu_x \geq 0`.

    From a probabilistic point of view, the force of mortality is defined as

    .. math::
        \mu_x = \lim_{\tau \to 0} \frac{Pr \left( x < T \leq x+\tau \mid T > x \right)}{\tau}

    where :math:`T` is the random variable describing the time-to-death (lifetime) of a newborn.

    The force of mortality can be used to calculate any survival probabilities:

    .. math::
        _np_x = e^{-\int_0^n \mu_{x+\tau} d\tau}.

    As life tables are given only for integer ages, we assume that the force of mortality is constant
    between two consecutive integer ages that is

    .. math::
        \mu_{x+\tau} = \mu_x = -\ln(p_x)

    for all :math:`x \in \mathbb{N}` and :math:`\tau \in [0,1)`.

    Parameters
    ----------
    x : numeric
        Age.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (non-negative)
        Force of mortality of an individual aged :math:`x`.

    Examples
    --------
    Compute :math:`\mu_{50}` according to the MR table:

    >>> force_of_mortality(50, "MR")
    0.003880

    Because we assume that the force of mortality is constant by age, this is the same as :math:`\mu_{50.3}` or :math:`\mu_{50.87}` for example:

    >>> force_of_mortality(50.3, "MR")
    0.003880 # same as mu_{50}
    >>> force_of_mortality(50.87, "MR")
    0.003880 # same as mu_{50}

    But this is different from :math:`\mu_{51}` because it is a new integer age and therefore a new force of mortality assumption:

    >>> force_of_mortality(51, "MR")
    0.004216 # different from mu_{50}
    """

    pass

def life_expectancy(x, table="XR", correction=0):
    r"""
    Compute the life expectancy :math:`e_x`.

    Note
    ----
    The life expectancy :math:`e_x` is the expected remaining lifetime of an individual aged :math:`x`.
    It is defined by

    .. math::
        e_x = \mathbb{E}[T_x] = \int_0^\infty {}_{\tau}p_x d\tau

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Parameters
    ----------
    x : numeric
        Age.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (non-negative)
        Life expectancy of an individual aged :math:`x`.

    Examples
    --------
    Compute the life expectancy of a newborn according to the MR table:

    >>> life_expectancy(0, "MR")
    77.71

    Compute :math:`e_{54.5}` according to the FK' table:

    >>> life_expectancy(54.5, "FK'")
    22.07 # a woman aged 54.5 years old will die on average at 76.57 years old (= 54.5 + 22.07)

    Compute :math:`e_{80}` according to the XR table with an age correction of -3 years:

    >>> life_expectancy(80, "XR", -3)
    11.41
    """

    pass

def pure_endowment(x, n=1, i=0, table="XR", correction=0):
    r"""
    Compute the present value of a pure endowment :math:`_nE_x`.

    Note
    ----
    A pure endowment consists of paying an amount of 1 unit in :math:`n` years from now
    to an individual currently aged :math:`x` if the individual survives.

    The present value is computed as

    .. math::
        _nE_x = \frac{_np_x}{(1+i)^n}

    where :math:`_np_x` is the probability that an individual aged :math:`x` survives in the
    next :math:`n` years and :math:`i` is the guaranteed interest rate.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric (non-negative)
        Present value of the pure endowment.

    Examples
    --------
    Compute :math:`E_{50}` according to the MR table with :math:`i=2\%`:

    >>> pure_endowment(50, 1, 0.02, "MR")
    0.9766

    Compute :math:`_{10.5}E_{54.5}` according to the FK' table with :math:`i=2\%`:

    >>> pure_endowment(54.5, 10.5, 0.02, "FK'")
    0.7139

    Compute :math:`_{5}E_{80}` according to the XR table with :math:`i=2\%` and an age correction of -3 years:

    >>> pure_endowment(80, 5, 0.02, "XR", -3)
    0.7262

    Finally, note that by definition the calculation of a pure endowment amounts exactly to discounting
    a survival probability. For example, the result of the example above can be obtained as follows:

    >>> survival_probability(80, 5, "XR", -3) / (1 + 0.02)^5
    0.7262
    """

    pass

def whole_life_annuity(x, i=0, table="XR", correction=0, beginning=False, freq=1):
    r"""
    Compute the present value of a whole life annuity :math:`a_x`.

    Note
    ----
    A whole life annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` is alive.

    If the payment frequency is annual, the present value is given by

    .. math::
        a_x = \sum_{k \geq 1} {}_kE_x = \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ...

    in the case of payments at the end of the year, or

    .. math::
        \ddot{a}_x = \sum_{k \geq 0} {}_kE_x = 1 + \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ...
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        a_x^{(m)} = \sum_{k \geq 1} {}_{\frac{k}{m}}E_x \qquad \text{and} \qquad \ddot{a}_x^{(m)} = \sum_{k \geq 0} {}_{\frac{k}{m}}E_x

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or :math:`m=4` for quarterly payments).

    Finally, we have the following relations:

    .. math::
        \ddot{a}_x = 1 + a_x \qquad \text{and} \qquad a_x = {}_na_x + {}_nE_x \cdot a_{x+n}.

    Parameters
    ----------
    x : numeric
        Age.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.
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
    Compute :math:`a_{50}` and :math:`\ddot{a}_{50}` according to the MR table with :math:`i=2\%`
    (the annuity is paid on a yearly basis):

    >>> whole_life_annuity(50, 0.02, "MR")
    21.68
    >>> whole_life_annuity(50, 0.02, "MR", TRUE)
    22.68

    Compute :math:`a_{54.5}^{(4)}` according to the FR table with :math:`i=2\%`
    (the annuity is paid on a quarterly basis):

    >>> whole_life_annuity(54.5, 0.02, "FR",,,4)
    89.34

    Compute :math:`\ddot{a}_{80}^{(12)}` according to the XR table with :math:`i=2\%` and an age correction of -3 years
    (the annuity is paid on a monthly basis):

    >>> whole_life_annuity(80, 0.02, "XR", -3, TRUE, 12)
    118.95
    """

    pass

def term_annuity(x, n=1, i=0, table="XR", correction=0, beginning=False, freq=1):
    r"""
    Compute the present value of a term annuity :math:`_na_x`.

    Note
    ----
    A term annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` is alive and with a maximum payment period of :math:`n` years.

    If the payment frequency is annual, the present value is given by

    .. math::
        _na_x = \sum_{k=1}^n {}_kE_x = \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ... + \frac{_np_x}{(1+i)^n}

    in the case of payments at the end of the year, or

    .. math::
        _n\ddot{a}_x = \sum_{k=0}^{n-1} {}_kE_x = 1 + \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ... + \frac{_{n-1}p_x}{(1+i)^{n-1}}
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        _na_x^{(m)} = \sum_{k=1}^{n \cdot m} {}_{\frac{k}{m}}E_x \qquad \text{and} \qquad _n\ddot{a}_x^{(m)} = \sum_{k=0}^{n \cdot m - 1} {}_{\frac{k}{m}}E_x

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or :math:`m=4` for quarterly payments).

    Finally, we have the following relations:

    .. math::
        _n\ddot{a}_x = 1 + {}_{n-1}a_x \qquad \text{and} \qquad _n\ddot{a}_x^{(m)} = 1 + {}_{n-\frac{1}{m}}a_x^{(m)}.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.
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
    Compute :math:`_{10}a_{50}` and :math:`_{10}\ddot{a}_{50}` according to the MR table with :math:`i=2\%`
    (the annuity is paid on a yearly basis):

    >>> term_annuity(50, 10, 0.02, "MR")
    8.74
    >>> term_annuity(50, 10, 0.02, "MR",, TRUE)
    8.97

    Compute :math:`_{10.5}a_{54.5}^{(4)}` according to the FR table with :math:`i=2\%`
    (the annuity is paid on a quarterly basis):

    >>> term_annuity(54.5, 10.5, 0.02, "FR",,,4)
    37.11

    Compute :math:`_{20}\ddot{a}_{80}^{(12)}` according to the XR table with :math:`i=2\%` and an age correction of -3 years
    (the annuity is paid on a monthly basis):

    >>> term_annuity(80, 20, 0.02, "XR", -3, TRUE, 12)
    116.38
    """

    pass

def whole_life_insurance(x, i=0, table="XR", correction=0, freq=1):
    r"""
    Compute the present value of a whole life insurance :math:`\bar{A}_x`.

    Note
    ----
    A whole life insurance consists of paying an amount of 1 unit when an individual aged :math:`x` dies.
    The formula assumes that the payment occurs at the middle of the period and not at the exact date of the death.

    If the period frequency is annual, the present value is given by

    .. math::
        \bar{A}_x = \sum_{k \geq 0} \frac{_kp_x \cdot q_{x+k}}{(1+i)^{k+0.5}} = \frac{q_x}{(1+i)^{0.5}} + \frac{p_x \cdot q_{x+1}}{(1+i)^{1.5}} + \frac{_2p_x \cdot q_{x+2}}{(1+i)^{2.5}} + ...

    If the period frequency is split (e.g., monthly period), the present value is given by

    .. math::
        \bar{A}_x^{(m)} = \sum_{k \geq 0} \frac{_\frac{k}{m}p_x \cdot {}_{\frac{1}{m}}q_{x+\frac{k}{m}}}{(1+i)^{\frac{k+0.5}{m}}}

    where :math:`m` is the period frequency (e.g., :math:`m=12` for monthly period or :math:`m=4` for quarterly period).

    Finally, we have the following relation:

    .. math::
        \bar{A}_x = {}_n\bar{A}_x + {}_nE_x \cdot \bar{A}_{x+n}.

    Parameters
    ----------
    x : numeric
        Age.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.
    freq : numeric
        Period frequency.
        The default assumes annual period.

    Returns
    -------
    numeric (non-negative)
        Present value of the whole life insurance.

    Examples
    --------
    Compute :math:`\bar{A}_{50}` according to the MK table with :math:`i=2\%`
    (the death benefit is paid at the middle of the year of the death):

    >>> whole_life_insurance(50, 0.02, "MK")
    0.6348

    Compute :math:`\bar{A}_{54.5}^{(4)}` according to the FK table with :math:`i=2\%`
    (the death benefit is paid at the middle of the quarter of the death):

    >>> whole_life_insurance(54.5, 0.02, "FK",,4)
    0.6312

    Compute :math:`\bar{A}_{80}^{(12)}` according to the XK table with :math:`i=2\%` and an age correction of -3 years
    (the death benefit is paid at the middle of the month of the death):

    >>> whole_life_insurance(80, 0.02, "XK", -3, 12)
    0.8690
    """

    pass

def term_insurance(x, n=1, i=0, table="XR", correction=0, freq=1):
    r"""
    Compute the present value of a term insurance :math:`_n\bar{A}_x`.

    Note
    ----
    A term insurance consists of paying an amount of 1 unit when an individual aged :math:`x` dies in the next :math:`n` years.
    The formula assumes that the payment occurs at the middle of the period and not at the exact date of the death.

    If the period frequency is annual, the present value is given by

    .. math::
        _n\bar{A}_x = \sum_{k=0}^{n-1} \frac{_kp_x \cdot q_{x+k}}{(1+i)^{k+0.5}} = \frac{q_x}{(1+i)^{0.5}} + \frac{p_x \cdot q_{x+1}}{(1+i)^{1.5}} + ... + \frac{_{n-1}p_x \cdot q_{x+n-1}}{(1+i)^{n-0.5}}.

    If the period frequency is split (e.g., monthly period), the present value is given by

    .. math::
        _n\bar{A}_x^{(m)} = \sum_{k=0}^{n \cdot m - 1} \frac{_\frac{k}{m}p_x \cdot {}_{\frac{1}{m}}q_{x+\frac{k}{m}}}{(1+i)^{\frac{k+0.5}{m}}}

    where :math:`m` is the period frequency (e.g., :math:`m=12` for monthly period or :math:`m=4` for quarterly period).

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    i : numeric
        Guaranteed interest rate.
    table : string
        Life table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.
    freq : numeric
        Period frequency.
        The default assumes annual period.

    Returns
    -------
    numeric (non-negative)
        Present value of the term insurance.

    Examples
    --------
    Compute :math:`_{10}\bar{A}_{50}` according to the MK table with :math:`i=2\%`
    (the death benefit is paid at the middle of the year of the death):

    >>> term_insurance(50, 10, 0.02, "MK")
    0.0971

    Compute :math:`_{10.5}\bar{A}_{54.5}^{(4)}` according to the FK table with :math:`i=2\%`
    (the death benefit is paid at the middle of the quarter of the death):

    >>> term_insurance(54.5, 10.5, 0.02, "FK",,4)
    0.0875

    Compute :math:`_{20}\bar{A}_{80}^{(12)}` according to the XK table with :math:`i=2\%` and an age correction of -3 years
    (the death benefit is paid at the middle of the month of the death):

    >>> term_insurance(80, 20, 0.02, "XK", -3, 12)
    0.8636
    """

    pass