# CSE565-Software-Verif-Validation-Test
## Developing Test Cases with DOE Tool
**Tool**: PICT
| Test Case | Type of Phone  | Authentication   | Connectivity | Memory | Battery Level |
| --------: | -------------- | ---------------- | ------------ | ------ | ------------- |
|       TC1 | iPhone 13      | Fingerprint      | 5G Edge      | 128 GB | 40 ~ 59%      |
|       TC2 | iPhone 14      | Text Password    | Wireless     | 512 GB | 80 ~ 100%     |
|       TC3 | Huawei Mate    | Face Recognition | 4G LTE       | 256 GB | 40 ~ 59%      |
|       TC4 | Google Pixel 7 | Fingerprint      | 3G           | 1 TB   | < 20%         |
|       TC5 | iPhone 13      | Text Password    | 4G LTE       | 1 TB   | 20 ~ 39%      |
|       TC6 | Google Pixel 7 | Face Recognition | Wireless     | 128 GB | 20 ~ 39%      |
|       TC7 | Galaxy Z       | Text Password    | 3G           | 256 GB | 80 ~ 100%     |
|       TC8 | Google Pixel 7 | Face Recognition | 5G Edge      | 512 GB | 60 ~ 79%      |
|       TC9 | Huawei Mate    | Text Password    | 3G           | 128 GB | 60 ~ 79%      |
|      TC10 | iPhone 13      | Fingerprint      | 4G LTE       | 512 GB | 80 ~ 100%     |
|      TC11 | iPhone 13      | Fingerprint      | Wireless     | 256 GB | 60 ~ 79%      |
|      TC12 | Google Pixel 7 | Text Password    | Wireless     | 1 TB   | 40 ~ 59%      |
|      TC13 | Huawei Mate    | Fingerprint      | 3G           | 512 GB | 20 ~ 39%      |
|      TC14 | Galaxy Z       | Face Recognition | 5G Edge      | 1 TB   | 60 ~ 79%      |
|      TC15 | iPhone 14      | Face Recognition | 5G Edge      | 256 GB | 20 ~ 39%      |
|      TC16 | Google Pixel 7 | Face Recognition | 4G LTE       | 128 GB | 80 ~ 100%     |
|      TC17 | iPhone 14      | Text Password    | 4G LTE       | 128 GB | < 20%         |
|      TC18 | Galaxy Z       | Fingerprint      | Wireless     | 512 GB | < 20%         |
|      TC19 | Galaxy Z       | Face Recognition | 3G           | 512 GB | 40 ~ 59%      |
|      TC20 | Huawei Mate    | Text Password    | 5G Edge      | 1 TB   | < 20%         |
|      TC21 | iPhone 14      | Fingerprint      | 4G LTE       | 1 TB   | 60 ~ 79%      |
|      TC22 | Huawei Mate    | Face Recognition | Wireless     | 1 TB   | 80 ~ 100%     |
|      TC23 | iPhone 13      | Face Recognition | 3G           | 256 GB | < 20%         |
|      TC24 | iPhone 14      | Text Password    | 3G           | 256 GB | 40 ~ 59%      |
|      TC25 | Galaxy Z       | Text Password    | 4G LTE       | 128 GB | 20 ~ 39%      |
|      TC26 | Google Pixel 7 | Text Password    | 5G Edge      | 256 GB | 80 ~ 100%     |

## Developing Test Cases with Gen AI Tool
**Tool**: ChatGPT
| Test Case | Type of Phone  | Authentication   | Connectivity | Memory | Battery Level |
| --------- | -------------- | ---------------- | ------------ | ------ | ------------- |
| TC1       | iPhone 14      | Fingerprint      | Wireless     | 128 GB | <20%          |
| TC2       | iPhone 13      | Face Recognition | 3G           | 256 GB | 20–39%        |
| TC3       | Galaxy Z       | Text Password    | 4G LTE       | 512 GB | 40–59%        |
| TC4       | Huawei Mate    | Fingerprint      | 5G Edge      | 1 TB   | 60–79%        |
| TC5       | Google Pixel 7 | Face Recognition | Wireless     | 512 GB | 80–100%       |
| TC6       | iPhone 13      | Text Password    | 4G LTE       | 128 GB | 60–79%        |
| TC7       | Galaxy Z       | Fingerprint      | 3G           | 1 TB   | <20%          |
| TC8       | Huawei Mate    | Face Recognition | Wireless     | 256 GB | 40–59%        |
| TC9       | Google Pixel 7 | Text Password    | 5G Edge      | 128 GB | 20–39%        |
| TC10      | iPhone 14      | Face Recognition | 4G LTE       | 1 TB   | 80–100%       |
| TC11      | Galaxy Z       | Text Password    | Wireless     | 256 GB | 60–79%        |
| TC12      | Huawei Mate    | Text Password    | 3G           | 512 GB | 20–39%        |
| TC13      | Google Pixel 7 | Fingerprint      | 5G Edge      | 256 GB | <20%          |
| TC14      | iPhone 14      | Text Password    | 3G           | 512 GB | 40–59%        |
| TC15      | iPhone 13      | Fingerprint      | 5G Edge      | 128 GB | 80–100%       |

## Comparison between Tools
| **Criterion**                 | **DOE Tool (Task 1)**                                                     | **Generative AI Tool (Task 2)**                                                |
| ----------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Number of Test Cases**      | 26 cases                                                                  | 15 cases                                                                       |
| **Coverage Guarantee**        | Ensures complete pairwise coverage for all parameter pairs                | Coverage may be incomplete; depends on AI prompt and random variation          |
| **Reliability / Consistency** | Deterministic and repeatable; same inputs always yield same set           | Non-deterministic; results may vary across prompts or sessions                 |
| **Ease of Generation**        | Requires setup (parameter input, DOE configuration)                       | Very fast; generated instantly with a single prompt                            |
| **Accuracy and Verification** | High accuracy; automatically validated for pairwise completeness          | Requires manual verification to ensure all pairs are covered                   |
| **Flexibility**               | Rigid parameter setup; harder to include natural-language constraints     | Highly flexible; constraints and preferences can be described in plain English |
| **Output Format**             | Structured table with clear test case order                               | May require formatting or cleanup for consistency                              |
| **Learning Curve**            | Moderate; user must understand DOE concepts                               | Low; anyone can prompt the AI without specialized knowledge                    |
| **Best Use Case**             | Formal software testing requiring guaranteed coverage and reproducibility | Early-stage brainstorming or exploratory test generation                       |
| **Overall Assessment**        | Most reliable and systematic approach                                     | Fastest and most adaptable but less rigorous                                   |

## DOE Tool Assessment (PICT)
### Features and Functionalities
The Microsoft PICT tool offers a robust and efficient solution for generating pairwise test cases based on combinatorial design. Its primary functionality lies in automatically creating a minimal set of test cases that ensures every pair of parameter values appears at least once. PICT also supports advanced features such as constraint handling, which allows users to exclude invalid or impossible combinations, and weighted parameters, which help prioritize certain values over others.

### Scope Covered by the Tool
The scope of PICT covers a wide range of combinatorial testing needs, from simple pairwise coverage to more complex n-wise configurations. In this project, PICT was applied to five parameters and each with multiple possible values. The full factorial design would have required 1,200 test cases, but PICT efficiently reduced this to only 26 test cases while maintaining complete pairwise coverage. This demonstrates the tool’s capability to significantly reduce testing effort without compromising test completeness. The results covered all logical pairwise interactions, making it suitable for both functional and configuration-based testing scenarios.

### Performance
PICT performed exceptionally well in terms of speed, accuracy, and consistency. The tool generated the full set of pairwise test cases almost instantly after providing the model file, showcasing its computational efficiency. It is deterministic, meaning that running the same model multiple times yields identical results, which is an essential feature for reproducible and traceable test design. PICT’s algorithm optimizes test generation by minimizing redundancy and ensuring even distribution of parameter combinations. Overall, its performance was highly reliable and consistent, producing results that align with the mathematical guarantees of the pairwise DOE technique.

### Ease of Use
While PICT is lightweight and fast, its and text-based model setup can pose a challenge for beginners unfamiliar with DOE concepts. Users must manually define all parameters and their possible values, which requires attention to syntax and formatting. However, once the initial setup is complete, generating test cases is straightforward. The output is in a clean tab-delimited format that can be easily imported into spreadsheets or documentation. Thus, while the learning curve is moderate, the tool is highly efficient and repeatable once mastered, making it a dependable choice for systematic test design.

## Gen AI Tools Assessment (ChatGPT)
Instead of manually defining parameters in a structured input file as required by PICT, I was able to describe the problem in natural language and asking ChatGPT to create a minimal set of pairwise test cases. The AI quickly produced a well-structured table containing 15 test cases that covered most combinations with minimal overlap. Crafting the prompt required some iteration; the initial output contained a few redundant or missing pairs, but refining the prompt with clearer instructions (such as “ensure every pair of parameter values appears at least once”) improved the results significantly. The generated test cases were easy to read and interpret, and formatting them into a spreadsheet or report required minimal post-processing. Overall, ChatGPT offered a fast, accessible, and user-friendly way to create test designs without needing prior knowledge of DOE tools.

The use of generative AI in software testing introduces a new level of speed, flexibility, and creativity to the test design process. While traditional DOE tools like PICT guarantee mathematical completeness, ChatGPT enables testers to explore and adjust test case designs rapidly through natural-language interaction. This is particularly useful in early development stages when requirements evolve frequently, or when human testers need quick drafts of test combinations for brainstorming or exploratory testing. Although AI-generated outputs may require manual verification to confirm full pairwise coverage, the productivity gains and reduced learning curve are substantial. In summary, ChatGPT demonstrates how generative AI can complement conventional DOE tools—offering agility and accessibility while accelerating the overall software testing workflow.
