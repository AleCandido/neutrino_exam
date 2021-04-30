# Neutrino project

## References

### Experimental measurements

1. [IceCube ultra-high-energy neutrinos `[IC17]`](https://inspirehep.net/literature/1637543)

### Theoretical predictions

1. (1998) Neutrino interactions at ultrahigh-energies [Gandhi `[oldLO]`](https://inspirehep.net/literature/472804)
  - very old paper **suggested**
  - LO cross sections, CTEQ4

2. (2010) Neutrino masses and mixings and... [Strumia, Vissani `[review]`](https://inspirehep.net/literature/718605)
  - review outdated, both arxiv version and website one updated in 2010
  - the "interesting" bibliography is `[48]`, a subset of this one
  - the "interesting" part is Chapter 4

3. Ultrahigh-energy neutrino nucleon cross-sections and perturbative
   unitarity [Kretzer et al. `[unitarity]`](https://inspirehep.net/literature/554276)
  - cited in `review`
  - applies analytic relations to bound the calculation
  - **interesting spin-off**
  - but it's old, *this also means there is room for a fast numerical update*,
    good job - low effort: they put a bound on the range of validity of
    perturbative expressions making use of the LO xs (and for sure an old
    unknown PDF set), than we can update reproducing the plot Fig.1 with the NLO
    CC DIS (and a newer PDF set)

4. Predictions for high energy neutrino cross-sections from the ZEUS global PDF
   fits [Cooper-Sarkar, Sarkar `[CSS]`](https://inspirehep.net/literature/765846)
  - cited in `review`
  - outdated in favor of 5 - `CSMS`

5. The high energy neutrino cross-section in the Standard Model and its
   uncertainty [Cooper-Sarkar, Mertsch, Sarkar `[CSMS]`](https://inspirehep.net/literature/914199)
  - make use of:
    - NLO CC DIS
    - CT10, HERAPDF1.5 (and consider MSTW2008)
    - not making use of small-x, claiming should be relevant
  - instead:
    - NNLO CC DIS is available by [Jun Gao](https://inspirehep.net/literature/1630481)
    - we have for sure better PDF sets at hand
    - small-x is available from [HELL](https://www.ge.infn.it/~bonvini/hell/)
      and implemented in APFEl
      - there also theories using it (like
        [155](https://docs.nnpdf.science/theory/theoryindex.html)) but no fit
        available in LHAPDF with NLL small-x
  - it's the **standard reference in all experimental papers**
    - the **suggested** exp-1 (`IC17`)
    - following papers

6. Complete predictions for high-energy neutrino propagation in matter [Rojo et
   al. `[Rojo]`](https://inspirehep.net/literature/1790834)
  - the most recent and relevant I could found
  - much more complete than all the others
  - not only including CC DIS, but also other relevant processes and models
