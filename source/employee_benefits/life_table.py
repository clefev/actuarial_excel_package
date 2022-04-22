def survivors(x, table=1, correction=0):
    r"""
    Compute the number of survivors :math:`l_x` according to the mortality table.

    Note
    ----
    The number of survivors at age :math:`x` is denoted by :math:`l_x`.

    If the age :math:`x` is given as an integer (e.g., :math:`x=50` for an individual aged 50 years old),
    then :math:`l_x` represents the number of people alive at age :math:`x` according to the mortality table.

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
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric
        Number of survivors.
    """

    pass

def deaths(x, n=1, table=1, correction=0):
    r"""
    Compute the number of deaths between age :math:`x` and :math:`x+n` according to the mortality table.

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
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric
        Number of deaths.
    """

    pass

def survival_probability(x, n=1, table=1, correction=0):
    r"""
    Compute the survival probability :math:`_np_x`.

    Note
    ----
    The survival probability :math:`_np_x` is the probability that an individual
    of age :math:`x` survives in the next :math:`n` years.
    It is computed as

    .. math::
        _np_x = \frac{l_{x+n}}{l_x}

    where :math:`l_x` is the number of people alive at age :math:`x`.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    table : string
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric between 0 and 1
        Probability that an individual aged :math:`x` survives in the next :math:`n` years.
    """

    pass

def death_probability(x, n=1, table=1, correction=0):
    r"""
    Compute the death probability :math:`_nq_x`.

    Note
    ----
    The death probability :math:`_nq_x` is the probability that an individual
    of age :math:`x` dies in the next :math:`n` years.
    It is computed as

    .. math::
        _nq_x = 1 - _np_x = \frac{l_x - l_{x+n}}{l_x}

    where :math:`l_x` is the number of people alive at age :math:`x`.

    Parameters
    ----------
    x : numeric
        Age.
    n : numeric
        Horizon time.
    table : string
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric between 0 and 1
        Probability that an individual aged :math:`x` dies in the next :math:`n` years.
    """

    pass

def expected_remaining_lifetime(x, table=1, correction=0):
    r"""
    Compute the expected remaining lifetime :math:`e_x`.

    Note
    ----
    The expected remaining lifetime of an individual aged :math:`x` is defined by

    .. math::
        e_x = \mathbb{E}[T_x]

    where :math:`T_x` is the random variable describing the remaining lifetime of an individual aged :math:`x`.

    Parameters
    ----------
    x : numeric
        Age.
    table : string
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric
        Expected remaining lifetime of an individual aged :math:`x`.
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
        Mortality table to use.
    correction : numeric
        Age correction. The correction can be positive (age increase) or negative (age reduction).
        The default assumes no correction.

    Returns
    -------
    numeric
        Present value of the pure endowment.
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
        Mortality table to use.
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
        Mortality table to use.
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
        Mortality table to use.
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
        Mortality table to use.
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
    """

    pass