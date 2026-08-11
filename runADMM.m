x = double(imread('ima-noisy.pgm'))/255;
myepsilon = 10^(-2);

results = zeros(8,3);
row = 1;

for t = 5:5:40

    [denoised, niter] = ADMM(x, t, myepsilon);

    norm_y = norm(denoised, "fro");

    results(row,1) = t;
    results(row,2) = niter;
    results(row,3) = norm_y;

    fprintf('t = %d, iterations = %d, norm = %.6f\n', t, niter, norm_y);

    if t == 20
        imwrite(uint8(denoised*255), 'denoised.pgm');
    end

    row = row + 1;

end

disp('      t      niter      norm');
disp(results);