.. _life.cohort_life_table:

Cohort life table
=================

.. toctree::
    :maxdepth: 1
    :hidden:

    force_of_mortality.rst
    survival_probability.rst
    death_probability.rst
    life_expectancy.rst
    pure_endowment.rst
    whole_life_annuity.rst
    term_annuity.rst
    whole_life_insurance.rst
    term_insurance.rst


.. warning::
    This module is in draft version.

This Excel add-in allows calculations on cohort life tables.

.. rubric:: :subtitle:`Conventions and notations`

The following conventions and notations will be used throughout the rest of the documentation:

    - All time units are expressed in years.
    - The age of an individual is denoted :math:`x` (e.g., :math:`x=50` for a 50 year old individual or :math:`x=50.75` for an individual aged 50 years and 9 months).
    - The calendar year is denoted :math:`t` (e.g., :math:`t=2022` for January 1, 2022 or :math:`t=2022.5` for July 1, 2022).
    - The guaranteed interest rate is yearly compounded and denoted :math:`i` (e.g., :math:`i=1.75\%`).

.. rubric:: :subtitle:`Probabilistic view`

The life expectancy of an individual can be studied from a probabilistic point of view as a random variable.
The random variable describing the time-to-death (lifetime) of a newborn born in calendar year :math:`t` is denoted :math:`T(t)`.
Therefore, the remaining lifetime of an individual aged :math:`x` in calendar year :math:`t` is given by the random variable:

.. math::
    T_x(t) = T(t-x) - x \mid T(t-x) > x,

that is the remaining lifetime of an individual born in calendar year :math:`t-x` (i.e. :math:`T(t-x) - x`)
given that the individual is still alive at age :math:`x` (i.e. knowing that :math:`T(t-x) > x`).

.. rubric:: :subtitle:`Force of mortality`

Life tables are modelled using forces of mortality (see :ref:`life.cohort_life_table.force_of_mortality`).
The force of mortality :math:`\mu_x(t)` depends on the age :math:`x` of the individual and the calendar year :math:`t`.
The tool assumes that the force of mortality is constant between two consecutive integer ages and calendar years that is

.. math::
    \mu_{x+\xi}(t+\tau) = \mu_x(t)

for all :math:`(x,t) \in \mathbb{N}^2` and :math:`(\xi,\tau) \in [0,1)^2`.
The most useful property of a force of mortality is to calculate survival probabilities through the following formula:

.. math::
    _np_x(t) = e^{-\int_0^n \mu_{x+\tau}(t+\tau) d\tau}.

The examples below illustrate how this works in the case of a constant force of mortality by age and calendar year.

.. admonition:: Example: calculations of survival probabilities

    The purpose of this example is to illustrate the calculation of the survival probabilities based on the assumption of
    a constant force of mortality by age and calendar year.
    We assume that an individual is subject to the following forces of mortality:

    .. list-table:: Force of mortality assumptions
        :header-rows: 1
        :stub-columns: 1
        :align: center

        *   - :math:`\mu_x(t)`
            - 2022
            - 2023
        *   - 65
            - 0.013
            - 0.011
        *   - 66
            - 0.014
            - 0.012

    #.  Compute the probability that an individual aged 65 in 2022 will survive the following year.
        Compare the result with an individual aged 65 in 2023.

            * :math:`p_{65}(2022) = e^{-\mu_{65}(2022)} = e^{-0.013} = 98.71\%`
            * :math:`p_{65}(2023) = e^{-\mu_{65}(2023)} = e^{-0.011} = 98.91\%`

    #.  Compute the probability that an individual aged 65 in 2022 will survive the following 6 months, 9 months, 18 months and 24 months.

            * :math:`_{0.5}p_{65}(2022) = e^{-0.5 \cdot \mu_{65}(2022)} = e^{-0.5 \cdot 0.013} = 99.35\%`
            * :math:`_{0.75}p_{65}(2022) = e^{-0.75 \cdot \mu_{65}(2022)} = e^{-0.75 \cdot 0.013} = 99.03\%`
            * :math:`_{1.5}p_{65}(2022) = e^{-(\mu_{65}(2022) + 0.5 \cdot \mu_{66}(2023))} = e^{-(0.013 + 0.5 \cdot 0.012)} = 98.12\%`
            * :math:`_{2}p_{65}(2022) = e^{-(\mu_{65}(2022) + \mu_{66}(2023))} = e^{-(0.013 + 0.012)} = 97.53\%`

    #.  Compute the probability that an individual aged 65 years and 9 months (i.e. :math:`x = 65 + \frac{9}{12} = 65.75`) in 2022
        will survive the following 2 months, 5 months and 10 months.

            * :math:`_{\frac{2}{12}}p_{65.75}(2022) = e^{-\frac{2}{12} \cdot \mu_{65}(2022)} = e^{-\frac{2}{12} \cdot 0.013} = 99.78\%`
            * :math:`_{\frac{5}{12}}p_{65.75}(2022) = e^{-(\frac{3}{12} \cdot \mu_{65}(2022) + \frac{2}{12} \cdot \mu_{66}(2023))} = e^{-(\frac{3}{12} \cdot 0.013 + \frac{2}{12} \cdot 0.012)} = 99.48\%`
            * :math:`_{\frac{10}{12}}p_{65.75}(2022) = e^{-(\frac{3}{12} \cdot \mu_{65}(2022) + \frac{7}{12} \cdot \mu_{66}(2023))} = e^{-(\frac{3}{12} \cdot 0.013 + \frac{7}{12} \cdot 0.012)} = 98.98\%`

    #.  Compute the probability that an individual aged 65 years and 9 months in the second quarter of 2022 (i.e. :math:`x = 65.75` and :math:`t = 2022.5`)
        will survive the following 10 months.

        .. math::
            \begin{align}
                _{\frac{10}{12}}p_{65.75}(2022.5) &= e^{-(\frac{3}{12} \cdot \mu_{65}(2022) + \frac{3}{12} \cdot \mu_{66}(2022) + \frac{4}{12} \cdot \mu_{66}(2023))} \\
                &= e^{-(\frac{3}{12} \cdot 0.013 + \frac{3}{12} \cdot 0.014 + \frac{4}{12} \cdot 0.012)} \\
                &= 98.93\%
            \end{align}


.. rubric:: :subtitle:`Life tables`

The life tables recognized by the module are listed below:

.. list-table:: List of cohort life tables
    :header-rows: 1
    :stub-columns: 1
    :align: center
    :widths: 20 80

    * - .. centered:: Name
      - .. centered:: Description
    * - IABE male
      - Best-estimate mortality projection for Belgian males (following IABE calibration from 2020).
    * - IABE female
      - Best-estimate mortality projection for Belgian females (following IABE calibration from 2020).

Documentation related to the IABE projections can be found here: https://iabe.be/expert-groups/output/output.
Finally, note that the ultimate age is set at 120 years and the mortality projections cover the calendar years from 2020 to 2140.