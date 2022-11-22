import unittest
from sys import getsizeof
from trivial_compression import CompressedGene


class TestTrivialComporession(unittest.TestCase):
    def test_compression(self):
        compressed_gene = CompressedGene("AAAA")
        self.assertLess(getsizeof(compressed_gene.bit_string), getsizeof("AAAA"))
        self.assertEqual(str(compressed_gene), "AAAA")

    def test_long_compression(self):
        gene_string = "ACGTAACCGGT" * 1000
        compressed_gene = CompressedGene(gene_string)
        self.assertLess(getsizeof(compressed_gene.bit_string), getsizeof(gene_string))
        self.assertEqual(compressed_gene._decompress(), gene_string)


if __name__ == "__main__":
    unittest.main()
