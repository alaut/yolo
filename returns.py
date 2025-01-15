import matplotlib.pyplot as plt
import numpy as np

sigma, mu = np.meshgrid(
    np.linspace(0, 2, 199)/100,
    np.linspace(0, 15, 201)/100,
)

sig = sigma*np.sqrt(252)


for Lmax in [2, 3]:
    fig, ax = plt.subplots()
    R = np.stack([L*mu - L**2*sig**2/2 for L in [1, Lmax]])

    dR = np.diff(R, axis=0).squeeze()*100
    dR[dR < 0] = np.nan

    pcm = ax.contourf(sigma*100, mu*100, dR)
    ax.plot(1, 10, 'rs', label='SPY (1% daily, 10% annual)')
    # X = np.linspace(0, 2, 100)/100
    # x = X*np.sqrt(252)

    # ax.plot(X*100, 100*0.5*x**2*(Lmax**2-1)/(Lmax-1))

    ax.set_title(f"$R=L\\mu-\\frac{{1}}{{2}}L^2 \\sigma^2$ : X{Lmax}")
    ax.set_xlabel('$\sigma_{daily}$ (%)')
    ax.set_ylabel('$\mu_{annual}$ (%)')
    ax.legend()

    fig.colorbar(pcm, ax=ax, label=f'$\Delta_{{1,{Lmax}}}$ (%)')
    fig.savefig(f"{Lmax}.png")


plt.show()
