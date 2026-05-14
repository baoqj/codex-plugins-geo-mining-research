# THMC Equation Library

## Flow

Mass balance:

```math
\partial(\rho \phi)/\partial t + \nabla \cdot (\rho q) = Q
```

Darcy law:

```math
q = -(k/\mu)(\nabla p - \rho g)
```

## Solute / Reactive Transport

```math
\partial(\phi C_i)/\partial t + \nabla \cdot (q C_i - \phi D \nabla C_i) = R_i
```

## Heat Transport

```math
(\rho C_p)_{eff} \partial T/\partial t + \rho_w C_w q \cdot \nabla T = \nabla \cdot (\lambda_{eff} \nabla T) + Q_T
```

## Mechanical Equilibrium

```math
\nabla \cdot \sigma + f = 0
```

Effective stress:

```math
\sigma' = \sigma - \alpha p I
```

## Chemical Source Terms

```math
R_i = R_i^{eq} + R_i^{kinetic} + R_i^{sorption} + R_i^{decay}
```

## Porosity / Permeability Feedback

Use only when required:

```math
k = k_0 f(\phi, a_f, damage)
```

