/* File add_vectors.c */

void add_vectors(double *result, double *vec1, double *vec2, int len)
{
    for (int i = 0 ; i < len ; i++) {
        result[i] = vec1[i] + vec2[i];
    }
}
