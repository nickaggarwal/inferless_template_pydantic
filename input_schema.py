INPUT_SCHEMA =  {
    "prompt": {
        "type": str,
        "required": true,
	      "shape": [1],
	      "example": ["There is a fine house in the forest"]
    },
    "negative_prompt": {
        "type": str,
        "required": false,
        "example": null,
	      "shape": [1]
    },
    "width": {
        "type": int,
        "required": false,
        "example": [ 768 ,  512 ],
	      "shape": [2]
    }
}
