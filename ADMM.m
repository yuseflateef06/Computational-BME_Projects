function [y_k, niter] = ADMM(x, t, myepsilon)

k = 0;
[M,N] = size(x);

y_k = x;

lambda_down_k = zeros(M-1,N);
lambda_right_k = zeros(M,N-1);

d_down_k = zeros(M-1,N);
d_right_k = zeros(M,N-1);

shall_continue = true;

while shall_continue == true

    k = k + 1;

    [d_down_kp1, d_right_kp1] = Update_D(lambda_down_k, lambda_right_k, y_k);

    y_kp1 = Update_Y(y_k, lambda_down_k, lambda_right_k, d_down_kp1, d_right_kp1, x, t);

    [lambda_down_kp1, lambda_right_kp1] = Update_Lambda(lambda_down_k, lambda_right_k, d_down_kp1, d_right_kp1, y_kp1);

    if norm(y_kp1 - y_k, "fro") <= myepsilon
        shall_continue = false;
    end

    y_k = y_kp1;
    d_down_k = d_down_kp1;
    d_right_k = d_right_kp1;
    lambda_down_k = lambda_down_kp1;
    lambda_right_k = lambda_right_kp1;

end

niter = k;

end