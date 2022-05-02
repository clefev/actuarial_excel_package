.. _employee_benefits.life_table:

Life table
==========

.. toctree::
    :maxdepth: 1
    :hidden:

    survivors.rst
    deaths.rst
    survival_probability.rst
    death_probability.rst
    expected_remaining_lifetime.rst
    pure_endowment.rst
    whole_life_annuity.rst
    term_annuity.rst
    whole_life_insurance.rst
    term_insurance.rst

.. warning::
    This module is in draft version.

The life table module of the Employee Benefits add-in allows you to perform calculations
related to life tables.

.. rubric:: :subtitle:`Conventions and notations`

The following conventions and notations will be used throughout the rest of the documentation:

    - All time units are expressed in years.
    - The current age of an individual is denoted :math:`x`.
    - The guaranteed interest rate is yearly compounded and denoted :math:`i`.

.. rubric:: :subtitle:`Probabilistic view`

The life expectancy of an individual can be studied from a probabilistic point of view as a random variable.
The random variable describing the time-to-death (from birth) is denoted :math:`T`.
Therefore, the remaining lifetime of an individual aged :math:`x` is given by the random variable:

.. math::
    T_x = T-x \mid T>x,

that is the remaining lifetime (i.e. :math:`T-x`) given that the individual is still alive at age :math:`x` (i.e. knowing that :math:`T>x`).

.. rubric:: :subtitle:`Life tables`

The life tables recognized by the module are listed below:

.. list-table:: List of life tables
    :header-rows: 1
    :stub-columns: 1
    :align: center
    :widths: 20 80

    * - .. centered:: Name
      - .. centered:: Description
    * - MR
      - Belgian regulatory table for male life operations
    * - FR
      - Belgian regulatory table for female life operations
    * - XR
      - Belgian regulatory table for unisex life operations
    * - MK
      - Belgian regulatory table for male death operations
    * - FK
      - Belgian regulatory table for female death operations
    * - FK'
      - Alternative table for female death operations including
        a higher mortality loading compared to the regulatory FK table
    * - XK
      - Belgian regulatory table for unisex death operations

These tables are calculated using the Makeham model. The Makeham model is a parametric model assuming
that the number of people alive at age :math:`x` is given by

.. math::
    l_x = k s^x g^{c^x}

where :math:`k>0`, :math:`s \in (0,1]`, :math:`g \in (0,1)` and :math:`c>1`.
The following parameters are used to build the Belgian regulatory tables:

.. list-table:: Parameters of the Makeham model
    :header-rows: 1
    :stub-columns: 1
    :align: center

    * - 
      - .. centered:: MR
      - .. centered:: FR
      - .. centered:: MK
      - .. centered:: FK
    * - :math:`k`
      - 1000266.63
      - 1000048.56
      - 1000450.59
      - 1000097.39
    * - :math:`s`
      - 0.999441703848
      - 0.999669730966
      - 0.999106875782
      - 0.999257048061
    * - :math:`g`
      - 0.999733441115
      - 0.999951440172
      - 0.999549614043
      - 0.999902624311
    * - :math:`c`
      - 1.101077536030
      - 1.116792453830
      - 1.103798111448
      - 1.118239062025

The alternative FK' table is defined in the same way as the FK table except that the parameter :math:`c`
is set to 1.122 (leading to an increase in mortality).
The unisex tables XR and XK are calculated for each integer age :math:`x` as an arithmetic average of
the MR-FR and MK-FK tables i.e.

.. math::
    l_x^{XR} = \frac{l_x^{MR} + l_x^{FR}}{2} \qquad \text{and} \qquad l_x^{XK} = \frac{l_x^{MK} + l_x^{FK}}{2}.

Finally, note that all of these tables are only calculated for integer ages :math:`x` (not for fractional ages)
and that the number of people alive :math:`l_x` is rounded to the nearest integer.
In the case of fractional ages, a linear interpolation is performed (see :ref:`employee_benefits.life_table.survivors`).
The ultimate age is :math:`x_{max} = 120` years old.

.. rubric:: :subtitle:`Age correction`

All the functions implemented in this module provide a possibility of age correction.
An age correction increases or decreases the actual age of an individual.
For instance, an age correction of -3 years assumes that an individual aged :math:`x` (real age)
is aged :math:`x-3` instead (corrected age) [#corrected_age]_.
Age corrections are used to provide a safety loading when performing actuarial calculations.
It is common practice to use a negative age correction (reduction) when calculating the present value of an annuity
with the MR/FR/XR tables.

.. [#corrected_age] In practice, the corrected age is calculated as :math:`\max(x + correction, 0)` to avoid negative ages when the correction is negative.