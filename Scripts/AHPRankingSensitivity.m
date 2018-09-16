numRows = height(AHP);
comp_matrix = [1, 1, 5/2, 15/4; 1, 1, 5/2, 15/4; 2/5, 2/5, 1, 3/2; 4/15, 4/15, 2/3, 1];
AHP1 = AHP(:,[7:10,1]);
mort_matrix = zeros(numRows, numRows);
patient_matrix = zeros(numRows, numRows);
psi_matrix = zeros(numRows, numRows);
spending_matrix = zeros(numRows, numRows);
for i=1:numRows
    for j = 1:numRows
        mort_matrix(i,j) = AHP1{i,1}/AHP1{j,1};
        patient_matrix(i,j) = AHP1{i,2}/AHP1{j,2};
        psi_matrix(i,j) = AHP1{i,3}/AHP1{j,3};
        spending_matrix(i,j) = AHP1{i,4}/AHP1{j,4};
    end
end
[mort_Weight, ~] = eig(mort_matrix);
[patient_Weight, ~] = eig(patient_matrix);
[psi_Weight, ~] = eig(psi_matrix);
[spending_Weight, ~] = eig(spending_matrix);
mort_Weight = mort_Weight(:,1);
patient_Weight = patient_Weight(:,1);
psi_Weight = psi_Weight(:,1);
spending_Weight = spending_Weight(:,1);
mort_Weight = mort_Weight./sum(mort_Weight);
patient_Weight = patient_Weight./sum(patient_Weight);
psi_Weight = psi_Weight./sum(psi_Weight);
spending_Weight = spending_Weight./sum(spending_Weight);
for i = 1:numRows
    AHP1{i,6} = 0.375*mort_Weight(i,1)+0.15*psi_Weight(i,1)+0.1*spending_Weight(i,1);
end
