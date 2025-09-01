import numpy as np

def test_preprocess_captions():
    # Mock captions
    captions = [np.array([b'hello world', b'test caption'])]
    result = preprocess_captions(captions)
    assert len(result) == 2
    assert result[0] == 'hello world'
    print("Test passed")

if __name__ == "__main__":
    test_preprocess_captions()
