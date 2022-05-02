def survivors(x, table=1, correction=0):
    r"""
    Compute the number of survivors :math:`l_x` according to the life table.

    Note
    ----
    The number of survivors at age :math:`x` is denoted by :math:`l_x`.

    If the age :math:`x` is given as an integer (e.g., :math:`x=50` for an individual aged 50 years old),
    then :math:`l_x` represents the number of people alive at age :math:`x` according to the life table.

    If the age :math:`x` is given as a decimal number (e.g., :math:`x=50.75` for an individual aged 50 years and 9 months),
    then :math:`l_x` is linearly interpolated as following

    .. math::
        l_x = (1-\tau) l_{\lfloor x \rfloor} + \tau l_{\lfloor x \rfloor + 1}

    where the age :math:`x = \lfloor x \rfloor + \tau` is split as an integer part and a decimal part
    (e.g., if :math:`x=50.75`, we have :math:`\lfloor x \rfloor = 50` and :math:`\tau=0.75`).

    The linear interpolation assumes an uniform distribution of deaths between two consecutive integer ages.

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
    numeric
        Number of survivors.

    Examples
    --------
    Compute :math:`l_{50}`, :math:`l_{51}` and :math:`l_{50.75}` according to the MR table:

    >>> survivors(50, "MR")
    941 273
    >>> survivors(51, "MR")
    937 628
    >>> survivors(50.75, "MR")
    938 539.25 # 0.25*941 273 + 0.75*937 628

    Compute :math:`l_{65}` according to the XR table with an age correction of -5 years
    (this is equivalent to compute :math:`l_{60}` without age correction as shown below):

    >>> survivors(65, "XR", -5)
    916 308
    >>> survivors(60, "XR")
    916 308
    """

    pass

def deaths(x, n=1, table=1, correction=0):
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
    numeric
        Number of deaths.

    Examples
    --------
    Compute :math:`d_{50}` according to the MR table:

    >>> deaths(50, 1, "MR")
    3 645

    Compute the number of deaths between age 54.5 and 65 according to the FK' table:

    >>> deaths(54.5, 10.5, "FK'")
    110 418.5

    Compute the number of deaths between age 80 and 85 according to the XR table with an age correction of -3 years:

    >>> deaths(80, 5, "XR", -3)
    137 040
    """

    pass

def survival_probability(x, n=1, table=1, correction=0):
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
    the random variable :math:`T_x`:

    .. math::
        Pr \left( T_x > n \right) = Pr \left( T > x+n | T > x \right) = {}_np_x

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Finally, note that we have the following decomposition formula

    .. math::
        _np_x = {}_tp_x \cdot {}_{n-t}p_{x+t}

    for all :math:`t \in (0,n)`.

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
    numeric between 0 and 1
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

def death_probability(x, n=1, table=1, correction=0):
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
    the random variable :math:`T_x`:

    .. math::
        Pr \left( T_x \leq n \right) = Pr \left( T \leq x+n | T > x \right) = {}_nq_x

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Finally, note that we have the following decomposition formula

    .. math::
        _nq_x = {}_tq_x + {}_tp_x \cdot {}_{n-t}q_{x+t}

    for all :math:`t \in (0,n)`.

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
    numeric between 0 and 1
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

def expected_remaining_lifetime(x, table=1, correction=0):
    r"""
    Compute the expected remaining lifetime :math:`e_x`.

    Note
    ----
    The expected remaining lifetime of an individual aged :math:`x` is defined by

    .. math::
        e_x = \mathbb{E}[T_x] = \int_0^\infty {}_tp_x dt

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
    numeric
        Expected remaining lifetime of an individual aged :math:`x`.

    Examples
    --------
    Compute the life expectancy of a new born according to the MR table:

    >>> expected_remaining_lifetime(0, "MR")
    77.71

    Compute :math:`e_{54.5}` according to the FK' table:

    >>> expected_remaining_lifetime(54.5, "FK'")
    22.08 # a woman aged 54.5 years old will die on average at 76.58 years old (= 54.5 + 22.08)

    Compute :math:`e_{80}` according to the XR table with an age correction of -3 years:

    >>> expected_remaining_lifetime(80, "XR", -3)
    11.42
    """

    pass

def pure_endowment(x, n=1, i=0, table=1, correction=0):
    r"""
    Compute the present value of a pure endowment :math:`_nE_x`.

    Note
    ----
    A pure endowment :math:`_nE_x` consists of paying an amount of 1 unit in :math:`n` years from now
    to an individual currently aged :math:`x` if the individual survives.

    The present value is computed as

    .. math::
        _nE_x = \frac{_np_x}{(1+i)^n}

    where :math:`_np_x` is the probability that an individual aged :math:`x` survives in the
    :math:`n` next years and :math:`i` is the guaranteed interest rate.

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
    numeric
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
    """

    pass

def whole_life_annuity(x, i=0, table=1, correction=0, beginning=False, freq=1):
    r"""
    Compute the present value of a whole life annuity :math:`a_x`.

    Note
    ----
    A whole life annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` is alive.

    If the payment frequency is annual, the present value is given by

    .. math::
        a_x = \sum_{t \geq 1} {}_tE_x = \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ...

    in the case of payments at the end of the year, or

    .. math::
        \ddot{a}_x = \sum_{t \geq 0} {}_tE_x = 1 + \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ...
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        a_x^{(m)} = \sum_{t \geq 1} {}_{\frac{t}{m}}E_x \qquad \text{and} \qquad \ddot{a}_x^{(m)} = \sum_{t \geq 0} {}_{\frac{t}{m}}E_x

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or
    :math:`m=4` for quarterly payments).

    Finally, we have the following relations:

    .. math::
        \ddot{a}_x = 1 + a_x \qquad \text{and} \qquad a_x = {}_na_x + {}_nE_x a_{x+n}.

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
    numeric
        Present value of the whole life annuity.

    Examples
    --------
    Compute :math:`a_{50}` and :math:`\ddot{a}_{50}` according to the MR table with :math:`i=2\%`
    (the annuity is paid on a yearly basis):

    >>> whole_life_annuity(50, 0.02, "MR")
    21.68
    >>> whole_life_annuity(50, 0.02, "MR",, TRUE)
    22.68

    Compute :math:`a_{54.5}^{(4)}` according to the FR table with :math:`i=2\%`
    (the annuity is paid on a quarterly basis):

    >>> whole_life_annuity(54.5, 0.02, "FR",,,4)
    89.36

    Compute :math:`\ddot{a}_{80}^{(12)}` according to the XR table with :math:`i=2\%` and an age correction of -3 years
    (the annuity is paid on a monthly basis):

    >>> whole_life_annuity(80, 0.02, "XR", -3, TRUE, 12)
    119.05
    """

    pass

def term_annuity(x, n=1, i=0, table=1, correction=0, beginning=False, freq=1):
    r"""
    Compute the present value of a term annuity :math:`_na_x`.

    Note
    ----
    A term annuity consists of a series of 1 unit payments for as long as an individual
    aged :math:`x` is alive and with a maximum payment period of :math:`n` years.

    If the payment frequency is annual, the present value is given by

    .. math::
        _na_x = \sum_{t=1}^n {}_tE_x = \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ... + \frac{_np_x}{(1+i)^n}

    in the case of payments at the end of the year, or

    .. math::
        _n\ddot{a}_x = \sum_{t=0}^{n-1} {}_tE_x = 1 + \frac{p_x}{1+i} + \frac{_2p_x}{(1+i)^2} + ... + \frac{_{n-1}p_x}{(1+i)^{n-1}}
    
    in the case of payments at the beginning of the year.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        _na_x^{(m)} = \sum_{t=1}^{n \cdot m} {}_{\frac{t}{m}}E_x \qquad \text{and} \qquad _n\ddot{a}_x^{(m)} = \sum_{t=0}^{n \cdot m - 1} {}_{\frac{t}{m}}E_x

    where :math:`m` is the number of payments per year (e.g., :math:`m=12` for monthly payments or
    :math:`m=4` for quarterly payments).

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
    numeric
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
    116.46
    """

    pass

def whole_life_insurance(x, i=0, table=1, correction=0, freq=1):
    r"""
    Compute the present value of a whole life insurance :math:`A_x`.

    Note
    ----
    A whole life insurance consists of paying an amount of 1 unit when an individual aged :math:`x` dies.
    The formula assumes that the payment occurs at the end of the period and not at the exact date of the death.

    If the payment frequency is annual, the present value is given by

    .. math::
        A_x = \sum_{t \geq 0} \frac{_tp_x \cdot q_{x+t}}{(1+i)^{t+1}} = \frac{q_x}{1+i} + \frac{_1p_x q_{x+1}}{(1+i)^2} + \frac{_2p_x q_{x+2}}{(1+i)^3} + ...

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        A_x^{(m)} = \sum_{t \geq 0} \frac{_\frac{t}{m}p_x \cdot {}_{\frac{1}{m}}q_{x+\frac{t}{m}}}{(1+i)^{\frac{t+1}{m}}}

    where :math:`m` is the payment frequency (e.g., :math:`m=12` for monthly payments or
    :math:`m=4` for quarterly payments).

    Finally, we have the following relation:

    .. math::
        A_x = {}_nA_x + {}_nE_x A_{x+n}.

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
        Payment frequency.
        The default assumes annual payment.

    Returns
    -------
    numeric
        Present value of the whole life insurance.

    Examples
    --------
    Compute :math:`A_{50}` according to the MK table with :math:`i=2\%`
    (the death benefit is paid at the end of the year of the death):

    >>> whole_life_insurance(50, 0.02, "MK")
    0.6286

    Compute :math:`A_{54.5}^{(4)}` according to the FK table with :math:`i=2\%`
    (the death benefit is paid at the end of the quarter of the death):

    >>> whole_life_insurance(54.5, 0.02, "FK",,4)
    0.6295

    Compute :math:`A_{80}^{(12)}` according to the XK table with :math:`i=2\%` and an age correction of -3 years
    (the death benefit is paid at the end of the month of the death):

    >>> whole_life_insurance(80, 0.02, "XK", -3, 12)
    0.8681
    """

    pass

def term_insurance(x, n=1, i=0, table=1, correction=0, freq=1):
    r"""
    Compute the present value of a term insurance :math:`_nA_x`.

    Note
    ----
    A term insurance consists of paying an amount of 1 unit when an individual aged :math:`x` dies within :math:`n` years.
    The formula assumes that the payment occurs at the end of the period and not at the exact date of the death.

    If the payment frequency is annual, the present value is given by

    .. math::
        _nA_x = \sum_{t=0}^{n-1} \frac{_tp_x \cdot q_{x+t}}{(1+i)^{t+1}} = \frac{q_x}{1+i} + \frac{_1p_x q_{x+1}}{(1+i)^2} + ... + \frac{_{n-1}p_x q_{x+n-1}}{(1+i)^n}.

    If the payment frequency is split (e.g., monthly payments), the present value is given by

    .. math::
        _nA_x^{(m)} = \sum_{t=0}^{n \cdot m - 1} \frac{_\frac{t}{m}p_x \cdot {}_{\frac{1}{m}}q_{x+\frac{t}{m}}}{(1+i)^{\frac{t+1}{m}}}

    where :math:`m` is the payment frequency (e.g., :math:`m=12` for monthly payments or
    :math:`m=4` for quarterly payments).

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
        Payment frequency.
        The default assumes annual payment.

    Returns
    -------
    numeric
        Present value of the term insurance.

    Examples
    --------
    Compute :math:`_{10}A_{50}` according to the MK table with :math:`i=2\%`
    (the death benefit is paid at the end of the year of the death):

    >>> term_insurance(50, 10, 0.02, "MK")
    0.0962

    Compute :math:`_{10.5}A_{54.5}^{(4)}` according to the FK table with :math:`i=2\%`
    (the death benefit is paid at the end of the quarter of the death):

    >>> term_insurance(54.5, 10.5, 0.02, "FK",,4)
    0.0873

    Compute :math:`_{20}A_{80}^{(12)}` according to the XK table with :math:`i=2\%` and an age correction of -3 years
    (the death benefit is paid at the end of the month of the death):

    >>> term_insurance(80, 20, 0.02, "XK", -3, 12)
    0.8626
    """

    pass