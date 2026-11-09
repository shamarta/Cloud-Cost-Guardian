# Market Validation

**Status:** Market validation paused; customer interviews are deferred while an educational prototype is built.
**Research snapshot:** 2026-11-09

## What we know so far

The market already has capable native and commercial cost-management products. A generic cloud-cost dashboard is not a defensible product position by itself.

- AWS Cost Explorer supports cost and usage analysis, forecasting, and Amazon Q explanations: [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/).
- AWS Cost Anomaly Detection uses machine learning and can explain anomalies by service, account, Region, and usage type. AWS documents that billing data can take up to 24 hours to appear and that a new service needs 10 days of history before it can be monitored: [AWS documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html).
- Vantage lists a free tier for up to $2,500 in tracked cloud spend and a $30/month Pro tier for up to $7,500, along with 40+ integrations and anomaly alerts: [Vantage pricing](https://www.vantage.sh/pricing).
- Finout describes a fixed annual fee based on committed cloud and AI spend, with custom quotes rather than public list prices: [Finout pricing](https://www.finout.io/pricing).
- The FinOps Foundation's framework describes the practice and its Inform, Optimize, and Operate phases; it is useful context, but not proof that a particular customer segment will buy this product: [FinOps Framework](https://www.finops.org/framework/).

These pages establish that there are existing alternatives and meaningful price pressure. They do **not** establish customer demand for Cloud Cost Guardian. No market-size, customer-demand, or savings statistic is assumed here.

## Initial customer hypothesis

Interview this segment first:

> **AWS-first AI startups with roughly 5–30 engineers, no dedicated FinOps hire, and a combined cloud and AI-infrastructure bill large enough that an unexpected increase matters.**

Potential pain to test: cost information is split across cloud and AI vendors, and the team cannot quickly explain which product, workload, or recent change caused a bill increase or what action is safe to take.

This is a hypothesis, not a differentiation claim. Vantage already advertises AI-provider integrations and LLM cost allocation, so “we show AWS and AI spend together” alone may not be enough. Interviews must uncover a recurring unmet need that teams cannot reasonably solve with their current provider consoles or existing products.

## Discovery plan

### Find 8–10 people to interview

Prioritize founders, CTOs, platform/DevOps engineers, or engineering leads at AWS-first AI startups. Ask about their current process and recent incidents; do not pitch a feature first.

### Interview questions

1. Tell me about the last time your cloud or AI bill was higher than expected.
2. How did you notice, and how long did it take to find the cause?
3. Which consoles, spreadsheets, alerts, or paid tools do you use today?
4. What part of that workflow is still manual or unreliable?
5. What did the unexpected spend or investigation cost the team?
6. Who owns this problem, and how often does it come up?
7. What have you already tried or paid for to address it?
8. Would you share a redacted example of a recent cost incident or a sample billing export for a follow-up?

Record the person's role and company type, the concrete incident, current workaround, frequency, impact, current spend/tool, and whether they agree to a follow-up. Separate direct quotes and observed facts from your interpretation.

### Commercial-product decision gate

The current prototype is a learning exercise, not evidence that the commercial product is validated. Before defining or marketing a paid product, conduct customer discovery and look for evidence of a repeated, costly problem.

Proceed to a narrow PRD only if:

- At least 3 interviewees independently describe the same recurring problem and a current workaround.
- At least 2 qualified interviewees agree to a concrete next step, such as a design-partner session, a read-only pilot, or sharing sample data.
- At least one potential customer expresses credible willingness to pay or agrees to evaluate a paid pilot. Compliments and hypothetical interest do not count.

If these conditions are not met, revisit the customer segment or problem before building.

## Candidate positioning to test

> **Find and explain unexpected AWS and AI-infrastructure cost changes before they become a billing surprise.**

Do not use this as a final product promise until interviews verify that buyers have the problem and that existing tools do not solve it adequately.

## First LinkedIn post draft

> امروز کار روی Cloud Cost Guardian را با کدنویسی شروع نکردم؛ با بررسی مسئله شروع کردم.
>
> ابزارهای قدرتمندی برای پایش هزینه‌های ابری وجود دارند، پس ساختن یک داشبورد دیگر به‌تنهایی کافی نیست. قبل از انتخاب قابلیت‌ها، می‌خواهم با تیم‌های فنی صحبت کنم و بفهمم آخرین بار که هزینه‌ی AWS یا سرویس‌های AI غیرمنتظره شد، چطور علتش را پیدا کردند و چه چیزی در فرایند فعلی‌شان جواب نداد.
>
> هدفم این است که محصول را از یک مشکل واقعی بسازم، نه از فرضیات خودم. اگر در یک استارتاپ AWS-first کار می‌کنید و با بررسی هزینه‌های ابری یا AI سروکار دارید، خوشحال می‌شوم تجربه‌تان را بشنوم.

## Sources

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Cost Anomaly Detection documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
- [AWS Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/)
- [Vantage pricing](https://www.vantage.sh/pricing)
- [Finout pricing](https://www.finout.io/pricing)
- [FinOps Foundation Framework](https://www.finops.org/framework/)
