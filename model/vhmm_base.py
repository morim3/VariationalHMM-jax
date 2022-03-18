import jax.numpy as jnp
from jax.scipy.special import logsumexp
from jax import lax


class VHMMBase:
    def __init__(self, cluster_num, initial_params):
        self.cluster_num = cluster_num
        self.params = initial_params.copy()
        pass

    def fit(self, X):
        pass

    def predict(self, X, viterbi=False):

        if not viterbi:
            return self.e_step(X)

        else:
            return self.viterbi(X)
        pass

    @staticmethod
    def _forward_one_step(prev_log_prob, trans_log_prob, obs_log_prob, ):
        '''
        :param prev_log_prob: jnp array, shape (batch_size, hidden_num)
        :param trans_log_prob: jnp array, shape (hidden_num, hidden_num)
        :param obs_log_prob: jnp array, shape (batch_size, hidden_num)
        :return:
        '''
        log_prob = jnp.expand_dims(prev_log_prob, axis=2) + trans_log_prob \
            + jnp.expand_dims(obs_log_prob, axis=2)
        return logsumexp(log_prob, axis=1)

    @staticmethod
    def _backward_one_step(next_log_prob, trans_log_prob, next_obs_log_prob):
        '''

        :param next_log_prob:
        :param trans_log_prob:
        :param next_obs_log_prob:
        :return:
        '''
        log_prob = jnp.expand_dims(next_log_prob, axis=2) + trans_log_prob + \ 
            jnp.expand_dims(next_obs_log_prob, axis=1)

        return logsumexp(log_prob, axis=2)

    @staticmethod
    def forward_step(init_log_prob, obs_log_probs, trans_log_prob):

        def scan_fn(log_prob, obs_log_prob):
            result = VHMMBase._forward_one_step(log_prob, trans_log_prob, obs_log_prob)
            return (
                result,
                result
            )

        forward_prob = lax.scan()
        pass

    @staticmethod
    def viterbi(X):
        pass
  
