# ChatGPT Finetuning（微调）  

## 文档
- [OPENAI 官网指导](https://platform.openai.com/docs/guides/fine-tuning)
- [微调具体应用](https://www.zhihu.com/question/523380224/answer/2894558776)

## 常用命令示例

微调转化数据集：
```bash
openai tools fine_tunes.prepare_data -f testdata.csv  
```

微调训练：
```bash
openai api fine_tunes.create -t testdata_prepared.jsonl -m ada -m curie: ft-< org >-< date >
```

监督微调情况：
```bash
openai api fine_tunes.follow -i ft-sWKDNnTmUyOGEdpvbAOvEaZt
```    

微调应用模型：
```bash
openai api completions.create -m ada:ft-personal-2023-04-25-07-37-10  -p faao
```   

微调删除模型：
```bash
openai api models.delete -i ada:ft-personal-2023-04-25-07-37-10
```

查看所有当前模型：
```bash
openai api fine_tunes.list
```

训练超参数：
```bash
# For multiclass classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes <N_CLASSES>

# For binary classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes 2 \
  --classification_positive_class <POSITIVE_CLASS_FROM_DATASET> 
```