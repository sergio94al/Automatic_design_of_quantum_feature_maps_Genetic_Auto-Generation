import numpy as np

class Circuit:

    def __init__(self, nqubits):
        self.nqubits = nqubits
        self.σx = np.array([[0.0,1.0],[1.0,0.0]]);
        self.σz = np.array([[1.0,0.0],[0.0,-1.0]]);
        self.σy = np.array([[0.0,-1j],[1.j,0.0]]);
        self.σ = np.array([np.eye(2), self.σx, self.σy, self.σz]);
        self.d = 2**nqubits
        self.H = np.array([[1,1],[1,-1]])/np.sqrt(2.0)

    def zero_state(self):
        ψ = np.zeros((self.d,))
        ψ[0] = 1.0
        return ψ

    def pauli_rotation(self, state, σ, θ, qubit):
        θ = np.asarray(θ).reshape(-1,1,1)/2.0
        M = θ.shape[0]
        U = np.cos(θ) * np.eye(2) - 1j * np.sin(θ) * σ
        Usame = U[:,[0,1],[0,1]].reshape(-1,2)
        Uoppo = U[:,[0,1],[1,0]].reshape(-1,2)
        di = 2**qubit
        dj = 2**(self.nqubits - qubit - 1)
        state = state.reshape(-1, dj, 2, di)
        state = Usame.reshape(M, 1, 2, 1) * state \
              + Uoppo.reshape(M, 1, 2, 1) * state[:, :, [1,0], :]
        if state.shape[0] == 1:
            return state.flatten()
        else:
            return state.reshape(-1, self.d)

    def h(self, state, qubit):
        di = 2**qubit
        s = state.shape
        state = state.reshape(-1, 2, di)
        return np.einsum('mjl,ji->mil', state, self.H).reshape(s)

    def x(self, state, qubit):
        di = 2**qubit
        s = state.shape
        state = state.reshape(-1, 2, di)
        return state[:,[1,0],:].reshape(s)

    def ry(self, state, θ, qubit):
        return self.pauli_rotation(state, self.σy, θ, qubit)

    def rx(self, state, θ, qubit):
        return self.pauli_rotation(state, self.σx, θ, qubit)

    def rz(self, state, θ, qubit):
        return self.pauli_rotation(state, self.σz, θ, qubit)

    def cx(self, state, qubit, target):
        assert self.nqubits >= 2
        assert 0 <= qubit <= self.nqubits
        assert 0 <= target <= self.nqubits
        assert target != qubit
        i = min(qubit, target)
        j = max(qubit, target)
        di = 2**i
        dj = 2**(j-i-1)
        dk = 2**(self.nqubits - j - 1)
        s = state.shape
        state = state.reshape(-1, 2, dj, 2, di).copy()
        if qubit > target:
            state[:,1,:,[1,0],:] = state[:,1,:,[0,1],:]
        else:
            state[:,[1,0],:,1,:] = state[:,[0,1],:,1,:]
        return state.reshape(s)
